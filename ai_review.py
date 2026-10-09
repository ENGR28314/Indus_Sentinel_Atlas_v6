"""AI review of SEBAL evapotranspiration submissions via Lovable AI Gateway.

Rule-based checks flag unusual values; the AI model explains patterns.
Requires env var LOVABLE_API_KEY (or Streamlit secret of the same name).
"""
import json
import os
from pathlib import Path

import pandas as pd
import requests

GATEWAY_URL = "https://ai.gateway.lovable.dev/v1/responses"
MODEL = "openai/gpt-6-astra"
STORE = Path(__file__).parent / "data" / "et_submissions.csv"

# Typical seasonal actual-ET range (mm/day) per sub-basin - approximate reference.
SUB_BASINS = {
    "Upper Indus (Gilgit-Baltistan)": (0.5, 3.5),
    "Kabul / Swat": (1.0, 4.5),
    "Jhelum (Mangla)": (1.5, 5.0),
    "Chenab (Marala-Trimmu)": (2.0, 6.0),
    "Ravi / Sutlej": (2.0, 6.5),
    "Lower Indus (Sindh canal command)": (2.5, 7.0),
    "Thal Doab": (1.0, 5.5),
    "Balochistan Kachhi Plain": (0.5, 5.0),
}
COLUMNS = ["sub_basin", "date", "mean_et_mm_day", "max_et_mm_day", "area_km2", "land_use", "notes"]


def load_submissions() -> pd.DataFrame:
    if STORE.exists():
        return pd.read_csv(STORE)
    return pd.DataFrame(columns=COLUMNS)


def save_submission(row: dict) -> pd.DataFrame:
    df = pd.concat([load_submissions(), pd.DataFrame([row])], ignore_index=True)
    STORE.parent.mkdir(exist_ok=True)
    df.to_csv(STORE, index=False)
    return df


def flag_values(df: pd.DataFrame) -> pd.DataFrame:
    """Add a 'flags' column with rule-based anomaly reasons."""
    out = df.copy()
    flags = []
    for _, r in out.iterrows():
        f = []
        lo, hi = SUB_BASINS.get(r["sub_basin"], (0.0, 8.0))
        m, mx = float(r["mean_et_mm_day"]), float(r["max_et_mm_day"])
        if m < 0 or mx < 0:
            f.append("negative ET")
        if m > 10 or mx > 12:
            f.append("physically implausible (> reference ET)")
        if m < lo * 0.5:
            f.append(f"mean far below typical {lo}-{hi}")
        elif m > hi * 1.3:
            f.append(f"mean far above typical {lo}-{hi}")
        if mx < m:
            f.append("max lower than mean")
        flags.append("; ".join(f))
    out["issues"] = flags
    # Statistical outliers within a sub-basin (needs >= 4 records)
    for b, g in out.groupby("sub_basin"):
        if len(g) >= 4:
            z = (g["mean_et_mm_day"] - g["mean_et_mm_day"].mean()) / (g["mean_et_mm_day"].std() or 1)
            for i in g.index[z.abs() > 2]:
                out.at[i, "issues"] = "; ".join(x for x in [out.at[i, "issues"], f"z={z[i]:.1f} outlier"] if x)
    return out


def _api_key():
    key = os.environ.get("LOVABLE_API_KEY")
    if not key:
        try:
            import streamlit as st
            key = st.secrets.get("LOVABLE_API_KEY")
        except Exception:
            key = None
    return key


class GatewayError(Exception):
    pass


ERROR_TEXT = {
    401: "AI key missing or invalid. Set LOVABLE_API_KEY.",
    402: "AI credits are used up. Add credits to the workspace.",
    403: "AI access is blocked for this workspace or model.",
    429: "Too many AI requests. Please wait a minute and try again.",
}


def stream_explanation(df: pd.DataFrame):
    """Yield text chunks of the AI explanation (streamed SSE)."""
    key = _api_key()
    if not key:
        raise GatewayError(ERROR_TEXT[401])
    records = df[COLUMNS + ["issues"]].fillna("").to_dict(orient="records")
    ranges = {k: f"{v[0]}-{v[1]} mm/day" for k, v in SUB_BASINS.items()}
    prompt = (
        "You are a hydrologist reviewing SEBAL actual evapotranspiration results for Indus Basin sub-basins "
        "(Pakistan). Using the records and typical ranges below: 1) explain water-use patterns across sub-basins "
        "and dates (crop season Rabi/Kharif, irrigation, canal supply, aridity); 2) list each unusual value, why it "
        "is suspicious, and likely causes (cloud contamination, bad hot/cold pixels, sensor issues, flooding, "
        "data entry); 3) give short practical actions for water managers. Use markdown headings, under 400 words.\n\n"
        f"Typical ranges: {json.dumps(ranges)}\nRecords (with rule-based flags): {json.dumps(records, default=str)}"
    )
    body = {
        "model": MODEL,
        "input": prompt,
        "stream": True,
        "store": False,
        "reasoning": {"effort": "low"},
    }
    headers = {
        "Authorization": f"Bearer {key}",
        "Lovable-API-Key": key,
        "X-Lovable-AIG-SDK": "fetch",
        "Content-Type": "application/json",
    }
    with requests.post(GATEWAY_URL, json=body, headers=headers, stream=True, timeout=(10, 300)) as r:
        if r.status_code != 200:
            try:
                msg = r.json().get("error", {}).get("message") or r.text
            except Exception:
                msg = r.text
            raise GatewayError(ERROR_TEXT.get(r.status_code, f"AI request failed ({r.status_code}): {msg[:300]}"))
        got = False
        for line in r.iter_lines(decode_unicode=True):
            if not line or not line.startswith("data:"):
                continue
            data = line[5:].strip()
            if data == "[DONE]":
                break
            try:
                ev = json.loads(data)
            except ValueError:
                continue
            if ev.get("type") == "response.output_text.delta":
                got = True
                yield ev.get("delta", "")
            elif ev.get("type") in ("response.failed", "error"):
                raise GatewayError("The AI model could not complete the review.")
        if not got:
            raise GatewayError("The AI model returned no explanation.")
