import unittest

from sandbox.shared import shared


class T(unittest.TestCase):
    def test_it(self):
        self.assertTrue(shared().startswith("lambda"))
