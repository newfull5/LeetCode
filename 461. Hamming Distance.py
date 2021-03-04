# Runtime: 28 ms, faster than 85.95% of Python3 online submissions for Hamming Distance.
# Memory Usage: 14.2 MB, less than 47.39% of Python3 online submissions for Hamming Distance.

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x^y).count('1')
