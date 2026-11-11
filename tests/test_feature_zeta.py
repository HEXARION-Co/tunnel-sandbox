import unittest

from sandbox.feature_zeta import zeta


class T(unittest.TestCase):
    def test_it(self):
        self.assertEqual(zeta(), "zeta-wrong")
