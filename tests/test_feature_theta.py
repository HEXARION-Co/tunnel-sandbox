import unittest

from sandbox.feature_theta import theta


class T(unittest.TestCase):
    def test_it(self):
        self.assertEqual(theta(), "theta")
