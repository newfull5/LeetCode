class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        return [b for a,b in sorted([(sum(arr), i) for i,arr in enumerate(mat)], key=lambda x: x[0])[:k]]
