"""Automated Unit Testing Engine. Run: python -m unittest test_suite.py"""
import unittest
import simulation_engine as se
import hydraulic_model as hm
import data_loader as dl


class TestBasinStress(unittest.TestCase):
    def test_balanced(self):
        self.assertAlmostEqual(se.calculate_basin_stress(1000, 1000, 100, 100), 1.0)

    def test_low(self):
        self.assertLess(se.calculate_basin_stress(2000, 500, 1000, 200), 0.5)

    def test_invalid(self):
        with self.assertRaises(ValueError):
            se.calculate_basin_stress(0, 10, 10, 10)


class TestWQI(unittest.TestCase):
    def test_pristine_excellent(self):
        self.assertEqual(se.wqi_status(se.water_quality_index(8.5, 7.2, 150, 2, 250)), "Excellent")

    def test_saline_collapse(self):
        self.assertEqual(se.wqi_status(se.water_quality_index(1.5, 9.5, 2500, 60, 5000)), "Ecosystem Collapse Warning")


class TestHazardClustering(unittest.TestCase):
    def test_extreme_flash_flood(self):
        self.assertEqual(se.classify_hazard(16000, 80), "Critical Hazard Warning")

    def test_nominal(self):
        self.assertEqual(se.classify_hazard(2000, 5), "Nominal")

    def test_synthesizer_critical(self):
        self.assertEqual(se.flash_flood_synthesizer("Lahore", 100).status, "Critical Hazard Warning")


class TestHydraulicsAndTelemetry(unittest.TestCase):
    def test_manning_positive(self):
        self.assertGreater(hm.manning_discharge(100, 4, 0.0002), 0)

    def test_telemetry_seasonality(self):
        df = dl.telemetry_12_months(end="2026-12-31")
        m = df.date.dt.month
        g = "Tarbela (Indus)"
        self.assertGreater(df[m == 7][g].mean(), df[m == 1][g].mean())


class TestSEBAL(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        import sebal_model as sb
        cls.sb = sb
        cls.r = sb.sebal_numpy(**sb.synthetic_indus_scene(80), doy=180, sun_elev=65)

    def test_energy_balance_closes(self):
        import numpy as np
        r = self.r
        self.assertTrue(np.allclose(r["LE"] + r["H"] + r["G"], r["Rn"], atol=1e-6))

    def test_anchor_pixels(self):
        r = self.r
        self.assertLess(r["H"][r["cold"]], 5)
        self.assertLess(r["EF"][r["hot"]], 0.1)

    def test_irrigated_more_et_than_desert(self):
        et = self.r["ET24"]
        self.assertGreater(et[:, :20].mean(), et[:, -20:].mean())

    def test_et_range(self):
        et = self.r["ET24"]
        self.assertTrue(0 <= et.min() and et.max() <= 15)

    def test_geopandas_volume(self):
        import geopandas as gpd
        from shapely.geometry import box
        gdf = gpd.GeoDataFrame({"ET24_mean": [5.0]}, geometry=[box(71, 31, 71.1, 31.1)], crs=4326)
        out = self.sb.add_volume_columns(gdf)
        self.assertAlmostEqual(out.area_km2[0], 106, delta=6)
        self.assertGreater(out.ET_volume_MCM_day[0], 0)


if __name__ == "__main__":
    unittest.main()
