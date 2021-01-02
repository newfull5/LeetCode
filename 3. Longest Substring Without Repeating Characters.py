class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        diction = {}
        answer = 0
        i = 0

        for j in range(len(s)):

            if s[j] in diction:
                i = max(diction[s[j]],i)

            answer = max(answer, j - i + 1)

            diction[s[j]] = j + 1

        return answer
