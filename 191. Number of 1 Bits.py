"""
# Runtime: 28 ms, faster than 90.42% of Python3 online submissions for Number of 1 Bits.
# Memory Usage: 14.3 MB, less than 43.11% of Python3 online submissions for Number of 1 Bits.

class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')
"""
# Runtime: 28 ms, faster than 90.42% of Python3 online submissions for Number of 1 Bits.
# Memory Usage: 14.3 MB, less than 43.11% of Python3 online submissions for Number of 1 Bits.

class Solution:
    def hammingWeight(self, n: int) -> int:
        return len(bin(n).replace('0',''))-1
