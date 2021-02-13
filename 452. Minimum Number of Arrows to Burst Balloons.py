class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points, key = lambda x: x[-1], reverse=True)

        cnt = 0

        while points:
            arrow_point = points.pop()[-1]
            if not points:
                cnt += 1
                break
            while True:
                if not points:
                    break
                if arrow_point >= points[-1][0]:
                    points.pop()
                else:
                    break
            cnt += 1
            
        return cnt
