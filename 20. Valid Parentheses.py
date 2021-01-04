"""
#2020.01.05
class Solution:
    def isValid(self, s: str) -> bool:
        
        for _ in range(10000):
            s = s.replace('()','')
            s = s.replace('[]','')
            s = s.replace('{}','')

        return s == ''
"""
class Solution:
    def isValid(self, s: str) -> bool:
        stack = [0]

        for n in s:
            if stack[-1] == '(' and n == ')':
                stack.pop()
            elif stack[-1] == '[' and n == ']':
                stack.pop()
            elif stack[-1] == '{' and n == '}':
                stack.pop()
            else:
                stack.append(n)

        return stack == [0]
