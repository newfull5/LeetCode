# Runtime: 6496 ms, faster than 17.74% of Python3 online submissions for Jump Game II.
# Memory Usage: 15.1 MB, less than 91.06% of Python3 online submissions for Jump Game II.

class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [float('inf')]*len(nums)
        dp[-1] = 0

        for i in range(len(nums)-2,-1,-1):
            for j in range(i+1, min(len(nums), i+nums[i]+1)):
                dp[i] = min(dp[i], dp[j]+1)

        return dp[0]
