class Solution:
    def climbStairs(self, n: int) -> int:
        import math

        f = math.factorial

        def C(a,b):
            if b == 0:
                return 1
            return int(f(a) / (f(a-b) * f(b)))


        k = 0
        sum = 0

        for i in range(0,(n//2)+1):
            sum += C(n-i,k+i)
            
        return sum
