# Runtime: 572 ms, faster than 55.92% of Python3 online submissions for Check If All 1's Are at Least Length K Places Away.
# Memory Usage: 17 MB, less than 60.57% of Python3 online submissions for Check If All 1's Are at Least Length K Places Away.

class Solution:
    def solution(self, nums, k):
        if nums.count(1) == 0:
            return True
        
        left = nums.index(1)

        for i in range(left, len(nums)):
            if nums[i] == 1 and left != i:
                distance = (i - left - 1)
                left = i
                if distance < k:
                    return False
        return True
    
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        return self.solution(nums, k)
