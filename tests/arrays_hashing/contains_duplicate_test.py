import unittest
from src.arrays_hashing.contains_duplicate import Solution

class ContainsDuplicateTest(unittest.TestCase):
  def setUp(self):
    self.solution = Solution()
  
  def test_contains_duplicate_true_when_repeated(self):
    nums1 = [1, 2, 3, 1]
    self.assertTrue(self.solution.containsDuplicate(nums1))
    nums2 = [1,1,1,3,3,4,3,2,4,2]
    self.assertTrue(self.solution.containsDuplicate(nums2))

  def test_contains_duplicate_false_when_non_repeated(self):
    nums1 = [1, 2, 3, 4]
    self.assertFalse(self.solution.containsDuplicate(nums1))

  def test_contains_duplicate_false_when_empty(self):
    nums1 = []
    self.assertFalse(self.solution.containsDuplicate(nums1))

if __name__ == '__main__':
    unittest.main()