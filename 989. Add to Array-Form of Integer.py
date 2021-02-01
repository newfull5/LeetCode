class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        A = map(str,A)

        A = (''.join(A))

        return list(map(int, (list(str(int(A) + K)))))
