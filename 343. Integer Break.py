# Runtime: 28 ms, faster than 87.82% of Python3 online submissions for Integer Break.
# Memory Usage: 14.4 MB, less than 19.03% of Python3 online submissions for Integer Break

class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        
        if n == 3:
            return 2
        
        def divide(n, divisor):
            arr = [n // divisor for _ in range(divisor)]    
            for i in range(n % divisor):
                arr[i] += 1

            return arr

        def mul(arr):
            answer = 1
            for num in arr:
                answer *= num

            return answer

        answer = 0

        for i in range(2, (n//2)+1):
            temp = mul(divide(n,i))

            if answer < temp:
                answer = temp
            else:
                break
                
        return answer
