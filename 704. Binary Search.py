# Runtime: 232 ms, faster than 83.25% of Python3 online submissions for Binary Search.
# Memory Usage: 15.5 MB, less than 91.49% of Python3 online submissions for Binary Search.

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        try:
            return nums.index(target)
        except ValueError:
            return -1
