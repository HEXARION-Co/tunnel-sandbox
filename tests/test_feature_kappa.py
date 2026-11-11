import unittest

from sandbox.feature_kappa import kappa


class T(unittest.TestCase):
    def test_it(self):
        self.assertEqual(kappa(), "kappa-wrong")
