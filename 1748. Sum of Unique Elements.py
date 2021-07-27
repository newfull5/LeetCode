# Runtime: 24 ms, faster than 99.00% of Python3 online submissions for Sum of Unique Elements.
# Memory Usage: 14.2 MB, less than 72.40% of Python3 online submissions for Sum of Unique Elements.

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        from collections import Counter

        answer = 0

        for a,b in Counter(nums).items():
            if b == 1:
                answer += a

        return answer
