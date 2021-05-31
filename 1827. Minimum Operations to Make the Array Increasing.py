# Runtime: 764 ms, faster than 5.51% of Python3 online submissions for Minimum Operations to Make the Array Increasing.
# Memory Usage: 15.1 MB, less than 23.55% of Python3 online submissions for Minimum Operations to Make the Array Increasing.

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        answer = 0

        while len(nums) != 1:
            if nums[0] < nums[1]:
                nums = nums[1:]
            else:
                answer += (nums[0] + 1) - nums[1]
                nums[1] = (nums[0] + 1)

        return answer
