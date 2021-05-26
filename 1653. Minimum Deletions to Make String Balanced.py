# Runtime: 404 ms, faster than 83.74% of Python3 online submissions for Minimum Deletions to Make String Balanced.
# Memory Usage: 15 MB, less than 86.75% of Python3 online submissions for Minimum Deletions to Make String Balanced.

class Solution:
    def minimumDeletions(self, s: str) -> int:
        n = len(s)
        a = 0
        res = 0

        for i in range(n-1,-1,-1):
            if s[i] == 'a':
                a += 1

            elif s[i] == 'b':
                if a > 0:
                    a -= 1
                    res += 1
        return res
