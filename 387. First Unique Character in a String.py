# Runtime: 100 ms, faster than 72.16% of Python3 online submissions for First Unique Character in a String.
# Memory Usage: 14.4 MB, less than 42.82% of Python3 online submissions for First Unique Character in a String.

class Solution:
    def firstUniqChar(self, s: str) -> int:
        from collections import Counter

        diction = Counter(s)

        for i,v in enumerate(s):
            if diction[v] == 1:
                return i
            
        return -1
