from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = defaultdict(list)

        for s in strs:
            char_count = [0] * 26 # a to z
            for c in s:
                char_count[ord(c) - ord('a')] += 1
            hash_map[tuple(char_count)].append(s)
        return hash_map.values()

if __name__ == '__main__':
    sol = Solution()
    sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"])
    sol.groupAnagrams([""])
    sol.groupAnagrams(["a"])