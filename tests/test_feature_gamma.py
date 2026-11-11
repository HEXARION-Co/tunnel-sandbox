import unittest

from sandbox.feature_gamma import gamma


class T(unittest.TestCase):
    def test_it(self):
        self.assertEqual(gamma(), "gamma-wrong")
