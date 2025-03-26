import unittest
from app import add, subtract, multiply, divide

class TestApp(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
    
    def test_subtract(self):
        self.assertEqual(subtract(5, 2), 3)
        
    def test_multiply(self):
        self.assertEqual(multiply(5, 3), 15)
        
    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)

if __name__ == "__main__":
    unittest.main()