# Runtime: 24 ms, faster than 97.04% of Python3 online submissions for Longer Contiguous Segments of Ones than Zeros.
# Memory Usage: 14.2 MB, less than 46.31% of Python3 online submissions for Longer Contiguous Segments of Ones than Zeros.

class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        return max(map(lambda x: len(x),s.split('1'))) < max(map(lambda x: len(x),s.split('0')))
