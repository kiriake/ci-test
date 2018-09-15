import unittest
from helloWorld import hello

class TestHelloWorld(unittest.TestCase):
  
  def test_hello(self):
    expected = "hello world"
    actual = hello()
    self.assertEqual(expected, actual)

if __name__ == "__main__":
  unittest.main()
