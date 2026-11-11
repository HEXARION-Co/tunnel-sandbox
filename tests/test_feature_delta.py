import unittest

from sandbox.feature_delta import delta


class T(unittest.TestCase):
    def test_it(self):
        self.assertEqual(delta(), "delta")
