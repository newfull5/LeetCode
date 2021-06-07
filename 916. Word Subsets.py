# Runtime: 1056 ms, faster than 39.24% of Python3 online submissions for Word Subsets.
# Memory Usage: 18.2 MB, less than 38.37% of Python3 online submissions for Word Subsets.

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        from collections import Counter

        cnt = Counter()

        for word in words2:
            cnt |= Counter(word)

        return [word for word in words1 if not cnt - Counter(word)]
