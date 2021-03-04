"""
# Runtime: 232 ms, faster than 83.25% of Python3 online submissions for Binary Search.
# Memory Usage: 15.5 MB, less than 91.49% of Python3 online submissions for Binary Search.

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        try:
            return nums.index(target)
        except ValueError:
            return -1
"""

# Runtime: 232 ms, faster than 83.25% of Python3 online submissions for Binary Search.
# Memory Usage: 15.6 MB, less than 70.14% of Python3 online submissions for Binary Search.        
        
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if nums[-1] < target:
            return -1
        
        if nums[0] > target:
            return -1
        
        left = 0
        right = len(nums)

        while left <= right:

            mid = (left + right) // 2

            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid -1

        if nums[left] == target:
            return (left)
        return (-1)        
