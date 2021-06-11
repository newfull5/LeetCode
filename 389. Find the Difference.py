# Runtime: 28 ms, faster than 95.29% of Python3 online submissions for Find the Difference.
# Memory Usage: 14.2 MB, less than 60.34% of Python3 online submissions for Find the Difference.

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        from collections import Counter

        temp = Counter(t) - Counter(s)

        return list(temp)[0]
