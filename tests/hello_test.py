import unittest
from pdm_hello_world.hello_world import hello

class TestHelloMethods(unittest.TestCase):
    def test_hello(self):
        expected = "Hello World, Jhon Doe !"
        test_hello = hello("Jhon Doe")
        self.assertEqual(test_hello, expected)


if __name__ == "__main__":
    unittest.main()

