# Runtime: 28 ms, faster than 77.72% of Python3 online submissions for Maximum 69 Number.
# Memory Usage: 14.1 MB, less than 67.68% of Python3 online submissions for Maximum 69 Number.

class Solution:
    def maximum69Number (self, num: int) -> int:
        num = list(str(num))

        for i in range(len(num)):
            if num[i] == '6':
                num[i] = '9'
                return int(''.join(num))
            
        return int(''.join(num))
