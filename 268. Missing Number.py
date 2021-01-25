"""
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        for i in range(max(nums)+2):
            if i not in nums:
                return i
"""
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = max(nums)
        answer = (n*(n + 1) // 2) - sum(nums)
        if answer == 0 and 0 in nums:
            return n+1
        return answer
