# Runtime: 32 ms, faster than 67.31% of Python3 online submissions for Reverse Substrings Between Each Pair of Parentheses.
# Memory Usage: 14.2 MB, less than 61.92% of Python3 online submissions for Reverse Substrings Between Each Pair of Parentheses.

class Solution:
    def reverseParentheses(self, s: str) -> str:
        from collections import deque

        right = deque(s)

        left = []

        while right:
            char = right.popleft()

            if char == ')':
                temp = []
                while True:
                    t = left.pop()
                    if t == '(':
                        break
                    temp.append(t)

                left += temp
            else:
                left.append(char)

        return ''.join(left)
