"""
#Runtime: 44 ms, faster than 85.74% of Python3 online submissions for Two Sum.
#Memory Usage: 14.4 MB, less than 46.77% of Python3 online submissions for Two Sum.
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return ([i,j])
"""
             
#Runtime: 48 ms, faster than 65.32% of Python3 online submissions for Two Sum.
#Memory Usage: 14.4 MB, less than 46.77% of Python3 online submissions for Two Sum.
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            if (target - nums[i]) in nums:
                if i != nums.index(target - nums[i]):
                    return [i, nums.index(target - nums[i])]
