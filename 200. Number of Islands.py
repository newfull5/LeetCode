# Runtime: 112 ms, faster than 99.76% of Python3 online submissions for Number of Islands.
# Memory Usage: 15.5 MB, less than 55.02% of Python3 online submissions for Number of Islands.

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def DFS(i,j):
            grid[i][j] = -1

            # to right
            if j != len(grid[0])-1 and grid[i][j+1] == '1':
                DFS(i,j+1)

            # to left
            if j != 0 and grid[i][j-1] == '1':
                DFS(i,j-1)

            #to up
            if i != 0 and grid[i-1][j] == '1':
                DFS(i-1, j)

            #to down
            if i != len(grid)-1 and grid[i+1][j] == '1':
                DFS(i+1, j)


        cnt = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):

                if grid[i][j] == '1':

                    cnt += 1
                    DFS(i,j)

        return cnt        
        
