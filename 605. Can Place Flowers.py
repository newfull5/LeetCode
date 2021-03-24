# Runtime: 160 ms, faster than 86.97% of Python3 online submissions for Can Place Flowers.
# Memory Usage: 15.5 MB, less than 8.58% of Python3 online submissions for Can Place Flowers.

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        import math

        flowerbed = [0] + flowerbed + [0]

        arr = [math.ceil((len(a) / 2) - 0.1)-1 for a in ''.join(map(str, flowerbed)).split('1')]

        return sum(arr) >= n
