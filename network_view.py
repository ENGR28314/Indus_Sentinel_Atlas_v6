"""Schematic upstream->downstream network of the Indus Basin (Plotly + NetworkX)."""
import networkx as nx
import plotly.graph_objects as go

EDGES = [
    ("Tarbela", "Jinnah", "Indus"), ("Jinnah", "Chashma", "Indus"), ("Chashma", "Taunsa", "Indus"),
    ("Taunsa", "Mithankot", "Indus"), ("Mithankot", "Guddu", "Indus"), ("Guddu", "Sukkur", "Indus"),
    ("Sukkur", "Kotri", "Indus"), ("Kotri", "Arabian Sea", "Indus"),
    ("Warsak", "Attock", "Kabul"), ("Attock", "Jinnah", "Indus"),
    ("Mangla", "Rasul", "Jhelum"), ("Rasul", "Trimmu", "Jhelum"),
    ("Marala", "Khanki", "Chenab"), ("Khanki", "Qadirabad", "Chenab"), ("Qadirabad", "Trimmu", "Chenab"),
    ("Trimmu", "Panjnad", "Chenab"), ("Balloki", "Sidhnai", "Ravi"), ("Sidhnai", "Panjnad", "Ravi"),
    ("Sulemanki", "Islam", "Sutlej"), ("Islam", "Panjnad", "Sutlej"), ("Panjnad", "Mithankot", "Panjnad"),
    # link canals
    ("Rasul", "Qadirabad", "Link"), ("Qadirabad", "Balloki", "Link"), ("Balloki", "Sulemanki", "Link"),
    ("Chashma", "Rasul", "Link"), ("Taunsa", "Panjnad", "Link"), ("Trimmu", "Sidhnai", "Link"), ("Marala", "Balloki", "Link"),
]

POS = {
    "Tarbela": (4, 10), "Attock": (3.4, 9.3), "Warsak": (2.2, 9.6), "Jinnah": (3.6, 8.4), "Chashma": (3.5, 7.6),
    "Taunsa": (3.4, 5.6), "Mithankot": (3.6, 3.8), "Guddu": (3.2, 3.2), "Sukkur": (2.8, 2.4), "Kotri": (2.6, 1.0),
    "Arabian Sea": (2.4, 0), "Mangla": (6, 9.6), "Rasul": (5.8, 8.6), "Trimmu": (5.6, 6.4),
    "Marala": (7.4, 9.0), "Khanki": (7.0, 8.4), "Qadirabad": (6.8, 7.9), "Panjnad": (5.2, 4.4),
    "Balloki": (8.0, 6.8), "Sidhnai": (6.8, 5.6), "Sulemanki": (8.6, 5.6), "Islam": (7.6, 4.8),
}
COLORS = {"Indus": "#1f4e79", "Kabul": "#2a9d8f", "Jhelum": "#e76f51", "Chenab": "#f4a261",
          "Ravi": "#8ab17d", "Sutlej": "#e9c46a", "Panjnad": "#264653", "Link": "#999999"}


def build_network():
    g = nx.DiGraph()
    for a, b, r in EDGES:
        g.add_edge(a, b, river=r)
    fig = go.Figure()
    for a, b, d in g.edges(data=True):
        (x0, y0), (x1, y1) = POS[a], POS[b]
        dash = "dot" if d["river"] == "Link" else "solid"
        fig.add_trace(go.Scatter(x=[x0, x1], y=[y0, y1], mode="lines", hoverinfo="text",
                                 text=d["river"], line=dict(color=COLORS[d["river"]], width=3, dash=dash), showlegend=False))
    fig.add_trace(go.Scatter(x=[POS[n][0] for n in g.nodes], y=[POS[n][1] for n in g.nodes], mode="markers+text",
                             text=list(g.nodes), textposition="middle right", marker=dict(size=12, color="#333")))
    fig.update_layout(height=750, xaxis=dict(visible=False), yaxis=dict(visible=False, title="Upstream -> Downstream"),
                      title="Indus Basin Schematic (dotted = link canals)", plot_bgcolor="white", showlegend=False)
    return fig
