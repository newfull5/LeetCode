# Runtime: 212 ms, faster than 40.56% of Python3 online submissions for N-Repeated Element in Size 2N Array.
# Memory Usage: 15.8 MB, less than 8.64% of Python3 online submissions for N-Repeated Element in Size 2N Array.

class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        return ([a for a,b in Counter(A).items() if b != 1][0])
