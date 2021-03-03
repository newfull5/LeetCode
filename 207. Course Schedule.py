# Runtime: 96 ms, faster than 77.19% of Python3 online submissions for Course Schedule.
# Memory Usage: 17.9 MB, less than 9.36% of Python3 online submissions for Course Schedule.

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        from collections import defaultdict

        visited = set()
        t = set()
        diction = defaultdict(list)

        for a,b in prerequisites:
            diction[a].append(b)

        def DFS(i):
            
            if i in t:
                return True

            if i in visited:
                return False

            visited.add(i)

            for num in diction[i]:
                if not DFS(num):
                    return False
            visited.remove(i)
            t.add(i)

            return True
        
        for x in list(diction):
            if not DFS(x):
                return False
            
        return True
