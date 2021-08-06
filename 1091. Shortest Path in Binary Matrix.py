from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid) -> int:

        n = len(grid)

        if grid[0][0] == 1:
            return -1

        if grid[n-1][n-1] == 1:
            return -1

        move_x = [0,0,1,-1,1,-1,1,-1]
        move_y = [1,-1,0,0,1,-1,-1,1]

        moves = [(move_x[i], move_y[i]) for i in range(8)]

        queue = deque([[0,0]])
        grid[0][0] = -1
        while queue:
            current = queue.popleft()

            for a, b in moves:
                x, y = current
                current_value = grid[x][y]

                # warning index error
                try:
                    if x+a < 0 or y+b < 0:
                        continue
                    next_cell = grid[x+a][y+b]
                except IndexError:
                    continue

                if next_cell == 0:
                    grid[x+a][y+b] = current_value -1
                    queue.append([x+a, y+b])

            if grid[n-1][n-1] != 0:

                return grid[n-1][n-1] * -1

        return -1



if __name__ == '__main__':
    grid = [[0,0,0],[1,1,1],[0,0,0]]

    sol = Solution()
    answer = sol.shortestPathBinaryMatrix(grid)

    print(answer)