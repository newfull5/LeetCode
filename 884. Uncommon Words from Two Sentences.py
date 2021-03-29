# Runtime: 32 ms, faster than 57.24% of Python3 online submissions for Uncommon Words from Two Sentences.
# Memory Usage: 14.2 MB, less than 84.21% of Python3 online submissions for Uncommon Words from Two Sentences.

class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        from collections import Counter

        arr = A.split() + B.split()

        return [a for a,b in Counter(arr).items() if b == 1]
