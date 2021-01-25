class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        while nums:
            temp = nums.pop()

            if temp in nums:
                nums.remove(temp)
            else:
                return temp
