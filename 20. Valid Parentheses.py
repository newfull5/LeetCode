class Solution:
    def isValid(self, s: str) -> bool:
        
        for _ in range(10000):
            s = s.replace('()','')
            s = s.replace('[]','')
            s = s.replace('{}','')

        return s == ''
