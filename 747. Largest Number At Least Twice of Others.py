# Runtime: 36 ms, faster than 65.25% of Python3 online submissions for Largest Number At Least Twice of Others.
# Memory Usage: 14.3 MB, less than 13.24% of Python3 online submissions for Largest Number At Least Twice of Others.

class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        max_ = max(nums)
        for num in nums:
            if num == max_:
                continue

            if num * 2 > max_:
                return -1
            
        return nums.index(max_)
