# Runtime: 28 ms, faster than 80.98% of Python3 online submissions for N-th Tribonacci Number.
# Memory Usage: 14 MB, less than 98.67% of Python3 online submissions for N-th Tribonacci Number.

class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n < 3:
            return 1
        a = 0
        b = 1
        c = 1
        
        for _ in range(n-2):
            a,b,c = b,c, a+b+c
            
        return c
