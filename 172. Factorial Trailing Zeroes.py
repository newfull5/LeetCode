class Solution:
    def trailingZeroes(self, n: int) -> int:
        from math import factorial as F
        
        if n == 0:
            return 0
        
        string = str(F(n))

        cnt = 0

        for i in range(len(string)-1,-1,-1):
            if string[i] == '0':
                cnt += 1
            else:
                break

        return cnt
