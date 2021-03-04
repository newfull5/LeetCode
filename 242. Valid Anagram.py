# Runtime: 40 ms, faster than 85.82% of Python3 online submissions for Valid Anagram.
# Memory Usage: 14.9 MB, less than 19.33% of Python3 online submissions for Valid Anagram.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
