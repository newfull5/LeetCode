#Runtime: 232 ms, faster than 89.79% of Python3 online submissions for Product of Array Except Self.
#Memory Usage: 22.5 MB, less than 17.97% of Python3 online submissions for Product of Array Except Self.

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_out = [1]
        right_out = [1]

        for i in range(len(nums)-1):
            left_out.append(nums[i] * left_out[-1])

        nums.reverse()

        for i in range(len(nums)-1):
            right_out.append(nums[i] * right_out[-1])

        right_out.reverse()

        return [left_out[i] * right_out[i] for i in range(len(nums))]
