import unittest
from reverse_string import reverse_string

class TestReverseString(unittest.TestCase):
    
    def test_normal_case(self):
        self.assertEqual(reverse_string("hello"), "olleh")
    
    def test_similar_case(self):
        self.assertEqual(reverse_string(""), "")

    def test_interesting_case(self):
        self.assertEqual(reverse_string("madam"), "madam")

if __name__ == "__name__":
    unittest.main()
    
    
