import unittest

from sandbox.feature_alpha import alpha


class T(unittest.TestCase):
    def test_it(self):
        self.assertEqual(alpha(), "alpha")
