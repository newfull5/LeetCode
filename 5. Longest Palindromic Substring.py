class Solution:
    def longestPalindrome(self, s: str) -> str:
        for i in range(len(s)+1):
            length = len(s) - i + 1

            for j in range(i):
                answer = s[j:j+length]
                if answer == answer[::-1]:
                    return answer
