import unittest

from sandbox.feature_epsilon import epsilon


class T(unittest.TestCase):
    def test_it(self):
        self.assertEqual(epsilon(), "epsilon")
