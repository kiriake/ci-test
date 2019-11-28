import unittest
from helloWorld import HelloWorld

class TestHelloWorld(unittest.TestCase):

    def test_hello(self):
        hello = HelloWorld()
        expected = "hello world"
        actual = hello.hello()
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()
