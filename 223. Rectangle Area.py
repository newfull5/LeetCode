# Runtime: 52 ms, faster than 70.02% of Python3 online submissions for Rectangle Area.
# Memory Usage: 14.6 MB, less than 22.07% of Python3 online submissions for Rectangle Area.

class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        if min(C, G) - max(A, E) < 0 or min(D, H) - max(B, F) < 0:            square = 0
        else:
            top = min(D,H)
            btm = max(B,F)
            right = min(C,G)
            left = max(A,E)

            square = (top - btm) * (right-left)

        return ((C-A)*(D-B)) + ((G-E)*(H-F)) - square
