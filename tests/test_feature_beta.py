import unittest

from sandbox.feature_beta import beta


class T(unittest.TestCase):
    def test_it(self):
        self.assertEqual(beta(), "beta")
