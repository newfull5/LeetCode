# Runtime: 40 ms, faster than 76.50% of Python3 online submissions for Search in Rotated Sorted Array.
# Memory Usage: 14.6 MB, less than 56.33% of Python3 online submissions for Search in Rotated Sorted Array.

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        try:
            return nums.index(target)
        except:
            return -1
