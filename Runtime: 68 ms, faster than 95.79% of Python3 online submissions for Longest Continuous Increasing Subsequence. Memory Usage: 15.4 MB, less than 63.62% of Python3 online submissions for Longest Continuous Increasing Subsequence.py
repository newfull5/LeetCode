# Runtime: 68 ms, faster than 95.79% of Python3 online submissions for Longest Continuous Increasing Subsequence.
# Memory Usage: 15.4 MB, less than 63.62% of Python3 online submissions for Longest Continuous Increasing Subsequence.

class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        answer = 0
        cnt = 1
        nums.append(-float('inf'))

        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                cnt += 1
            else:
                answer = max(answer, cnt)
                cnt = 1

        return answer
