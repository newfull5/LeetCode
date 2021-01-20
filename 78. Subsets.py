class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        from itertools import combinations

        answer = []

        for i in range(0,len(nums)+1):
            answer += (list(map(lambda x: list(x), list(combinations(nums,i)))))

        return answer
