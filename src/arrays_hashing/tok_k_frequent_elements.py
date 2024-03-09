from collections import defaultdict
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = {}
        freq_to_elements = [[] for i in range(len(nums) + 1)]
        for num in nums:
            frequencies[num] = 1 + frequencies.get(num, 0)
        
        for key, value in frequencies.items():
            freq_to_elements[value].append(key)

        res = []

        for i in range(len(freq_to_elements) - 1, 0, -1):
            for n in freq_to_elements[i]:
                res.append(n)
                if len(res) == k:
                    return res


if __name__ == '__main__':
    sol = Solution()
    sol.topKFrequent([1,1,1,2,2,3], 2)
    sol.topKFrequent([1], 1)