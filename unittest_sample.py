import unittest
from program import calculate
 
class TestUM(unittest.TestCase):
 
    def setUp(self):
        pass
 
    def test_numbers_3_4(self):
        self.assertEqual(calculate(3,4), 7)
 
if __name__ == '__main__':
    unittest.main()