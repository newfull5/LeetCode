# Runtime: 56 ms, faster than 61.41% of Python3 online submissions for Top K Frequent Words.
# Memory Usage: 14.3 MB, less than 66.00% of Python3 online submissions for Top K Frequent Words.

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        from collections import Counter

        diction = Counter(words).items()

        diction = sorted(diction, key=lambda x:x[0])

        diction = sorted(diction, key=lambda x:x[1], reverse=True)

        answer = [diction[i][0] for i in range(k)]

        return answer
