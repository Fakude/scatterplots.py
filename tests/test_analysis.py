import unittest

from analyse_study_time import fit_line, make_data


class StudyTimeTests(unittest.TestCase):
    def test_data_is_deterministic(self):
        self.assertTrue(make_data(2, 10).equals(make_data(2, 10)))

    def test_fit_returns_positive_relationship_for_example(self):
        slope, _intercept, correlation = fit_line(make_data())
        self.assertGreater(slope, 0)
        self.assertGreater(correlation, 0)


if __name__ == "__main__":
    unittest.main()
