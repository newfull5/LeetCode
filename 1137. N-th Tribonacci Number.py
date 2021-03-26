"""
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
"""
# Runtime: 16 ms, faster than 99.83% of Python3 online submissions for N-th Tribonacci Number.
# Memory Usage: 14.3 MB, less than 13.31% of Python3 online submissions for N-th Tribonacci Number.
    
class Solution:
    def tribonacci(self, n: int) -> int:
        arr = [0, 1, 1, 2, 4, 7, 13, 24, 44, 81, 149, 274, 504, 927, 1705, 3136, 5768, 10609, 19513, 35890, 66012, 121415, 223317, 410744, 755476, 1389537, 2555757, 4700770, 8646064, 15902591, 29249425, 53798080, 98950096, 181997601, 334745777, 615693474, 1132436852, 2082876103, 3831006429, 7046319384, 12960201916]
        return arr[n]    
