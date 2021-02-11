"""
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        
        import math

        return (math.log(n, 2) - int(math.log(n, 2))) < 1e-10
     
"""        
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        
        import numpy as np

        return np.log2(n) == int(np.log2(n))
