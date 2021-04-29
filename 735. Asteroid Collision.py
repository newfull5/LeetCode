# Runtime: 160 ms, faster than 8.25% of Python3 online submissions for Asteroid Collision.
# Memory Usage: 15.6 MB, less than 20.28% of Python3 online submissions for Asteroid Collision.

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        start = 0

        while True:

            for i in range(start, len(asteroids)-1):
                
                left = asteroids[i]
                right = asteroids[i+1]

                if left >= 0 and right <= 0:

                    if abs(left) == abs(right):
                        del asteroids[i]
                        del asteroids[i]

                        start = max(i-1,0)
                        break

                    elif abs(left) > abs(right):
                        del asteroids[i+1]

                        start = i
                        break

                    elif abs(left) < abs(right):
                        del asteroids[i]

                        start = max(i-1,0)
                        break

            else:
                break
                
        return asteroids
