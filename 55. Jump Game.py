# Runtime: 92 ms, faster than 36.63% of Python3 online submissions for Jump Game.
# Memory Usage: 16.2 MB, less than 52.11% of Python3 online submissions for Jump Game.

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
               return True
        
        for i,v in enumerate(nums):
            if i + v == len(nums) -1:
                return True
            
            if v == 0:

                for j in range(i,-1,-1):
                    if i < nums[j] + j:
                        break

                else:
                    return False

        return True
