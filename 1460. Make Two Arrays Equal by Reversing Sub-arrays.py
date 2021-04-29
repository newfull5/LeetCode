# Runtime: 68 ms, faster than 98.47% of Python3 online submissions for Make Two Arrays Equal by Reversing Sub-arrays.
# Memory Usage: 14.4 MB, less than 87.62% of Python3 online submissions for Make Two Arrays Equal by Reversing Sub-arrays.

class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        return sorted(target) == sorted(arr)
