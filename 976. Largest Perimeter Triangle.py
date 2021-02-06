class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        A = sorted(A, reverse=True)

        for i in range(len(A)-2):
            triangle = A[i:i+3]
            if triangle[0] >= triangle[1] + triangle[2]:
                continue
            return sum(triangle)
        return 0
