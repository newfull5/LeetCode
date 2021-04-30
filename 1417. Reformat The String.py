# Runtime: 44 ms, faster than 65.45% of Python3 online submissions for Reformat The String.
# Memory Usage: 14.4 MB, less than 37.04% of Python3 online submissions for Reformat The String.

class Solution:
    def reformat(self, s: str) -> str:
        import re

        digits = re.compile('\d')
        letters = re.compile('[a-z]')

        letters = letters.findall(s)
        digits = digits.findall(s)

        if abs(len(digits) - len(letters)) > 1:
            return ''

        answer = ''

        for _ in range(min(len(digits), len(letters))):
            answer += digits.pop()
            answer += letters.pop()

        if letters:
            answer = letters[0] + answer
        if digits:
            answer += digits[0]

        return answer
