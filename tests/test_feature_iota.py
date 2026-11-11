import unittest

from sandbox.feature_iota import iota


class T(unittest.TestCase):
    def test_it(self):
        self.assertEqual(iota(), "iota")
