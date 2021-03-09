# Runtime: 20 ms, faster than 99.44% of Python3 online submissions for Reverse Words in a String.
# Memory Usage: 14.2 MB, less than 88.68% of Python3 online submissions for Reverse Words in a String.

class Solution:
    def reverseWords(self, s: str) -> str:
        answer = ''

        s = s.strip()

        for string in s.split()[::-1]:
            answer += string
            answer += ' '

        return answer[:-1]
