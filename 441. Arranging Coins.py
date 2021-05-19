# Runtime: 764 ms, faster than 50.86% of Python3 online submissions for Arranging Coins.
# Memory Usage: 14.1 MB, less than 67.06% of Python3 online submissions for Arranging Coins.

class Solution:
    def arrangeCoins(self, n: int) -> int:
        answer = 0

        for i in range(100000000):
            answer += i
            if answer > n:
                return i-1
