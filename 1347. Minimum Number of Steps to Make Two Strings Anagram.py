class Solution:
    def minSteps(self, s: str, t: str) -> int:
        from collections import Counter

        s = Counter(s)
        t = Counter(t)

        answer = 0

        for k in t:
            if t[k] > s[k]:
                answer += t[k] - s[k]

        return answer