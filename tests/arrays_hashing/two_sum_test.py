import unittest
from src.arrays_hashing.two_sum import Solution

class TwoSumTest(unittest.TestCase):
  def setUp(self):
    self.solution = Solution()

  def test_indexes_target_9_2_7(self):
    self.assertTrue(self.solution.twoSum([2,7,11,15], 9))
  
  def test_returns_indexes_target_6_2_4(self):
    self.assertTrue(self.solution.twoSum([3,2,4], 6))

  def test_returns_indexes_target_6_3_3(self):
    self.assertTrue(self.solution.twoSum([3,3], 6))


if __name__ == '__main__':
    unittest.main()