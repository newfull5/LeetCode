# Runtime: 5680 ms, faster than 5.21% of Python3 online submissions for Increasing Subsequences.
# Memory Usage: 21.6 MB, less than 80.50% of Python3 online submissions for Increasing Subsequences.

class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        answer = []

        def DFS(current, nums, max_index):
            if current not in answer and len(current) > 1:
                answer.append(current)

            if not nums:
                return

            for i in range(max_index,len(nums)):
                if current + [nums[i]] == sorted(current + [nums[i]]):
                    copy = nums[:]
                    copy.remove(nums[i])
                    DFS(current+[nums[i]],copy,i)

        DFS([],nums,0)

        return answer
