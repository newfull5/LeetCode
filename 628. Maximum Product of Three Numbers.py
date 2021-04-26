# Runtime: 272 ms, faster than 17.04% of Python3 online submissions for Maximum Product of Three Numbers.
# Memory Usage: 15.7 MB, less than 6.57% of Python3 online submissions for Maximum Product of Three Numbers.

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        
        if len(nums) == 3:
            return nums[0] * nums[1] * nums[2]
        
        if max(nums) < 0:
            nums = sorted(nums)
            return nums[-1] * nums[-2] * nums[-3]
        
        nums.sort()

        nump = []
        numn = []

        for num in nums:
            if num >= 0:
                nump.append(num)
            else:
                numn.append(num)
                
        if len(numn) >=2 and len(nump) >= 1:
            answer1 = numn[0] * numn[1] * nump[-1]
        
        if len(nump) >=3:
            answer2 = nump[-1] * nump[-2] * nump[-3]

        try:
            return max(answer1,answer2)
        except:
            pass
        
        try:
            answer1
        except NameError:
            return answer2
        
        try:
            answer2
        except NameError:
            return answer1
        
        
