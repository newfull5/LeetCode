# Runtime: 324 ms, faster than 94.74% of Python3 online submissions for Find All Numbers Disappeared in an Array.
# Memory Usage: 26 MB, less than 6.64% of Python3 online submissions for Find All Numbers Disappeared in an Array.

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        return set(range(1, len(nums)+1)) - set(nums)
