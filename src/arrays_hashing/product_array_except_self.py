from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = 1
        output = [1] * len(nums)
        for i in range(len(nums)):
            output[i] = res
            res *= nums[i]
        res = 1
        for i in range(len(nums) - 1, -1, -1):
            output[i] *= res
            res *= nums[i]
        return output
    
    def productExceptSelf2(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = [0] * n
        right = [0] * n
        result = [0] * n

        left[0] = 1
        for i in range(1, n):
            left[i] = left[i - 1] * nums[i - 1]

        right[n - 1] = 1
        for i in range(n - 2, -1, -1):
            right[i] = right[i + 1] * nums[i + 1]

        for i in range(n):
            result[i] = left[i] * right[i]

        return result