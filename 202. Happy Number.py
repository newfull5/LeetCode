class Solution:
    def isHappy(self, n: int) -> bool:
        visited = []

        while n != '1':
            n = str(sum(map(lambda x: int(x)**2, (list(str(n))))))
            if n in visited:
                return False
            visited.append(n)
            
        return True
