#Runtime: 6360 ms, faster than 5.11% of Python3 online submissions for Max Number of K-Sum Pairs.
#Memory Usage: 27.2 MB, less than 66.80% of Python3 online submissions for Max Number of K-Sum Pairs.

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        from collections import Counter

        answer = 0

        diction = Counter(nums)

        keys = list(diction.keys())

        while keys:
            num = keys.pop()

            if (k - num) <= 0:
                continue

            if num == k/2:
                answer += (diction[num] // 2)

            elif (k - num) in keys:
                answer += min(diction[k-num], diction[num])
                keys.remove(k-num)

        return answer
