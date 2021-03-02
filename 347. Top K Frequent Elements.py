class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter

        diction = Counter(nums)

        diction = sorted(diction.items(), key = lambda x: x[-1], reverse = True)

        return [a for a,b in diction[:k]]        
