import unittest

from sandbox.hello import hello


class HelloTest(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(hello("Tunnel"), "Bonjour Tunnel")


if __name__ == "__main__":
    unittest.main()
