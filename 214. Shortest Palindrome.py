class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if s == '':
            return ''
        
        if len(s) == 1 or s == s[::-1]:
            return s

        sr = s[::-1]
        for i in range(1,len(s)):
            if (sr[i:] == s[:-i]):
                return (sr[:i] + s)
