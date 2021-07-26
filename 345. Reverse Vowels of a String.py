# Runtime: 64 ms, faster than 49.64% of Python3 online submissions for Reverse Vowels of a String.
# Memory Usage: 15.2 MB, less than 49.77% of Python3 online submissions for Reverse Vowels of a String.

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a','e','i','o','u','A','E','I','O','U']
        s = list(s)
        arr = []

        for i in range(len(s)):
            if s[i] in vowels:
                arr.append(s[i])
                s[i] = '_'

        for i in range(len(s)):
            if s[i] == '_':
                s[i] = arr.pop()

        return ''.join(s)
