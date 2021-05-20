# Runtime: 88 ms, faster than 50.41% of Python3 online submissions for Counting Bits.
# Memory Usage: 21 MB, less than 41.79% of Python3 online submissions for Counting Bits.

class Solution:
    def countBits(self, num: int) -> List[int]:
        return [bin(i).count('1') for i in range(num+1)]
