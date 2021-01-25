class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        while nums:
            temp = nums.pop()
            if temp in nums:
                return temp
