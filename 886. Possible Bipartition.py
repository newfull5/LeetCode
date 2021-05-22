# Runtime: 696 ms, faster than 76.48% of Python3 online submissions for Possible Bipartition.
# Memory Usage: 20.1 MB, less than 57.26% of Python3 online submissions for Possible Bipartition.

class Solution:
    def possibleBipartition(self, N, dislikes):
        
        bag = [[] for i in range(N+1)]
        visited = [-1] * (N+1)
        count = 0
        for dislike in dislikes:
            bag[dislike[0]].append(dislike[1])
            bag[dislike[1]].append(dislike[0])
        
        for i in range(1, N+1):
            if visited[i] == -1 and  len(bag[i]) > 0:
                if not self.visit(0, i, bag, visited):
                    return False
                
        return True
      
    def visit(self, curLevel, i, bag, visited):     
        if visited[i] >= 0:
            return (curLevel - visited[i]) % 2 == 0
                
        visited[i] = curLevel
        for des in bag[i]:
            if not self.visit(curLevel + 1, des, bag, visited):
                return False
        return True
