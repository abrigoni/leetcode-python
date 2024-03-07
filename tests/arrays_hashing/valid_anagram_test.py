import unittest
from src.arrays_hashing.valid_anagram import Solution

class ValidAnagramTest(unittest.TestCase):
  def setUp(self):
    self.solution = Solution()

  def test_true_when_valid(self):
    str1 = 'anagram'
    str2 = 'nagaram'
    self.assertTrue(self.solution.isAnagram(str1, str2))
  
  def test_false_when_invalid(self):
    str1 = 'anagram'
    str2 = 'nabaram'
    self.assertFalse(self.solution.isAnagram(str1, str2))

  def test_false_on_distinct_length(self):
    str1 = 'anagram'
    str2 = 'a'
    self.assertFalse(self.solution.isAnagram(str1, str2))

  def test_true_on_empty_strings(self):
    str1 = ''
    str2 = ''
    self.assertTrue(self.solution.isAnagram(str1, str2))

if __name__ == '__main__':
    unittest.main()