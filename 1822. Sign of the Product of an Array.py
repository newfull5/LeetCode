# Runtime: 84 ms, faster than 11.68% of Python3 online submissions for Sign of the Product of an Array.
# Memory Usage: 14.3 MB, less than 67.70% of Python3 online submissions for Sign of the Product of an Array.

class Solution:
    def arraySign(self, nums: List[int]) -> int:
        
        prod = 1
        
        for num in nums:
            prod *= num
            
        if prod == 0:
            return 0
        if prod > 0:
            return 1
        return -1
