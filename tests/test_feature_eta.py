import unittest

from sandbox.feature_eta import eta


class T(unittest.TestCase):
    def test_it(self):
        self.assertEqual(eta(), "eta")
