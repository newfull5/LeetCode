"""
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False

        for i in range(0, 1000000):
            if 3**i == n:
                return True
            if 3**i > n:
                return False

        return False
"""


class Solution:
    def reculsive(self, n):
        n, rem = divmod(n, 3)
        
        if rem != 0:
            return False
        if n == 1:
            return True
        return self.reculsive(n)

    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        if n == 1:
            return True
        return self.reculsive(n)
