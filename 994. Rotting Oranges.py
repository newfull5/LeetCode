from collections import deque


class Solution:
    @staticmethod
    def check_all_rotten(grid):
        for arr in grid:
            if 1 in arr:
                return False
        return True

    def orangesRotting(self, grid) -> int:
        if Solution.check_all_rotten(grid):
            return 0

        m = len(grid)
        n = len(grid[0])
        start = []
        visited = []
        move = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    start.append((i, j))

        queue = deque(start)
        visited += start
        answer = -1

        while queue:
            answer += 1
            length = len(queue)
            for _ in range(length):
                current_h, current_w = queue.popleft()

                for x, y in move:
                    if current_h+x < 0 or current_w+y < 0:
                        continue
                    try:
                        after_move = grid[current_h+x][current_w+y]
                    except IndexError:
                        continue

                    if after_move == 1:

                        if (current_h+x, current_w+y) not in visited:
                            queue.append((current_h+x, current_w+y))
                            visited.append((current_h+x, current_w+y))
                        grid[current_h+x][current_w+y] = 2

        if Solution.check_all_rotten(grid):
            return answer
        return -1
