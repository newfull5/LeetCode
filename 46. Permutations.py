class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        from itertools import permutations

        return list(map(lambda x: list(x), list(permutations(nums))))
