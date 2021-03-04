# Runtime: 36 ms, faster than 82.75% of Python3 online submissions for Largest Number.
# Memory Usage: 14.2 MB, less than 83.93% of Python3 online submissions for Largest Number.

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        max_len = len(str(max(nums)))
        return str(int(''.join([b for a,b in sorted(map(lambda x: (str(x) * max_len, str(x)) ,nums), reverse=True)])))
