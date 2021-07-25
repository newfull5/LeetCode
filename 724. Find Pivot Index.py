# Runtime: 8508 ms, faster than 5.14% of Python3 online submissions for Find Pivot Index.
# Memory Usage: 15.5 MB, less than 6.73% of Python3 online submissions for Find Pivot Index.

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        for pivot in range(len(nums)):
            left, right = nums[:pivot], nums[pivot+1:]

            if sum(left) == sum(right):
                return pivot
            
        return -1
