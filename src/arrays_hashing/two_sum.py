from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for i in range(len(nums)):
            # a + b = target
            # a = target - b
            # search a in hashset, if exists return
            b = nums[i]
            if (target - b) in hash_map:
                return [hash_map.get(target-b),i]
            else:
                hash_map[nums[i]] = i