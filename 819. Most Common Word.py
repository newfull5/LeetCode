class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        import re
        import collections

        paragraph = (re.sub('[^a-zA-Z\s]',' ',paragraph)).lower().split()

        for a,b in sorted(collections.Counter(paragraph).items(), key = lambda x: x[1], reverse=True):
            if a not in banned:
                return a
