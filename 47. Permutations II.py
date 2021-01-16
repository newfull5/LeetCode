class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        from itertools import permutations
        
        lists = []
        
        for num in list(map(lambda x: list(x), list(permutations(nums)))):
            if not num in lists:
                lists.append(num)
                
        return lists
