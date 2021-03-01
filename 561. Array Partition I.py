#Runtime: 264 ms, faster than 69.51% of Python3 online submissions for Array Partition I.
#Memory Usage: 16.7 MB, less than 95.99% of Python3 online submissions for Array Partition I.

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()

        return sum([nums[i] for i in range(0,len(nums),2)])
