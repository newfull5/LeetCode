# Runtime: 36 ms, faster than 89.98% of Python3 online submissions for Permutations.
# Memory Usage: 14.3 MB, less than 90.99% of Python3 online submissions for Permutations.

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        from itertools import permutations as P

        return list(map(lambda x: list(x), P(nums)))
