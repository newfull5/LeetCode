# Runtime: 32 ms, faster than 49.90% of Python3 online submissions for Score of Parentheses.
# Memory Usage: 14.4 MB, less than 10.41% of Python3 online submissions for Score of Parentheses.

class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        from collections import deque

        S = S.replace('()','1')

        stack = []

        S = deque(S)

        while S:

            s = S.popleft()

            stack.append(s)

            try:
                if stack[-3] == '(' and stack[-2].isdigit() and stack[-1] == ')':
                    stack.pop()
                    temp = int(stack.pop())
                    stack.pop()
                    stack.append(str(temp*2))

                if stack[-1].isdigit() and stack[-2].isdigit():
                    stack.append(str(int(stack.pop()) + int(stack.pop())))

            except IndexError:
                pass


        while len(stack) != 1:
            stack.append(str(int(stack.pop())+int(stack.pop())))
        return int(stack[0])
