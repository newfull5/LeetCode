# Runtime: 1308 ms, faster than 43.35% of Python3 online submissions for Maximum Erasure Value.
# Memory Usage: 27.5 MB, less than 81.26% of Python3 online submissions for Maximum Erasure Value.

class Solution:
    def maximumUniqueSubarray(self, nums):
        beg, end, S, n, sm = 0, 0, set(), len(nums), 0
        ans = 0
        while end < n:
            if nums[end] not in S:
                sm += nums[end]
                S.add(nums[end])
                end += 1
                ans = max(ans, sm)
            else:
                sm -= nums[beg]
                S.remove(nums[beg])
                beg += 1
        
        return ans 
