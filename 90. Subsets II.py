class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        from itertools import combinations

        answer = [[]]
        for i in range(1, len(nums)+1):
            for num in (combinations(nums, i)):
                num = sorted(list(num))
                if num not in answer:
                    answer.append(num)
        return answer
