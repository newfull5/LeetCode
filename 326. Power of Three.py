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
