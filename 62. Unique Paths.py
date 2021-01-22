class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        import math
        
        m = m-1
        n = n-1
        
        return int(math.factorial(m+n) / (math.factorial(m) * math.factorial(n)))
