class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return list(map(lambda x: list(x), list(combinations(range(1,n+1),k))))
