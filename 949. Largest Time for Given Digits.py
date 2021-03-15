# Runtime: 32 ms, faster than 76.19% of Python3 online submissions for Largest Time for Given Digits.
# Memory Usage: 14.3 MB, less than 59.52% of Python3 online submissions for Largest Time for Given Digits.

class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        from itertools import permutations as P

        h,m = -1,-1

        for a in list(P(arr)):
            hour = a[0] * 10 + a[1]
            minute = a[2] * 10 + a[3]
            if hour < 24 and minute < 60:
                if hour > h:
                    h,m = hour,minute
                elif hour == h and minute > m:
                    m = minute
                    
        if h == -1 and m == -1:
            return ''
        
        if len(str(h)) == 1:
            h = '0' + str(h)
            
        if len(str(m)) == 1:
            m = '0' + str(m)
            
        return str(h)+':'+str(m)
