# Runtime: 36 ms, faster than 34.32% of Python3 online submissions for Add Digits.
# Memory Usage: 14.3 MB, less than 44.61% of Python3 online submissions for Add Digits

class Solution:
    def addDigits(self, num: int) -> int:
        while num > 10:
            num = sum([int(n) for n in str(num)])

        return num
