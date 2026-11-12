import unittest

from sandbox.hello import hello, hello_twice


class HelloTest(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(hello("Tunnel"), "Bonjour Tunnel")

    def test_hello_twice(self):
        self.assertEqual(hello_twice("Tunnel"), "Bonjour Tunnel / Bonjour Tunnel")
        self.assertEqual(hello_twice(""), "Bonjour  / Bonjour ")


if __name__ == "__main__":
    unittest.main()
