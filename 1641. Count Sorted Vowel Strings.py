# Runtime: 32 ms, faster than 64.79% of Python3 online submissions for Count Sorted Vowel Strings.
# Memory Usage: 14.5 MB, less than 16.77% of Python3 online submissions for Count Sorted Vowel Strings.

class Solution:
    def countVowelStrings(self, n: int) -> int:
        seen = {}
        def dp(n, k):
            if k == 1 or n == 1: return k
            if (n, k) in seen:
                return seen[n, k]
            seen[n, k] = sum(dp(n - 1, k) for k in range(1, k + 1))
            return seen[n, k]
        return dp(n, 5)
