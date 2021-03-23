# Runtime: 72 ms, faster than 85.90% of Python3 online submissions for K-diff Pairs in an Array.
# Memory Usage: 15.8 MB, less than 47.49% of Python3 online submissions for K-diff Pairs in an Array.

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if k == 0:
            from collections import Counter
            return len([num for num in Counter(nums).values() if num >= 2])
        
        answer = 0

        diction = dict()

        for num in nums:
            diction[num] = 1

        for num in diction.keys():
            try:
                if diction[num+k]:
                    answer += 1

            except KeyError:
                continue

        return answer
