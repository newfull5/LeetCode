# Runtime: 208 ms, faster than 34.89% of Python3 online submissions for Valid Mountain Array.
# Memory Usage: 15.6 MB, less than 52.33% of Python3 online submissions for Valid Mountain Array.

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        
        for i in range(len(arr)-1):
            if arr[i] == arr[i+1]:
                return False
        
        idx = arr.index(max(arr))

        left = arr[:idx]

        right = arr[idx+1:]

        if not left or not right:
            return False

        if len(left) >= 2:
            for i in range(len(left)-1):
                if left[i] >= left[i+1]:
                    return False

        if len(right) >= 2:
            for i in range(len(right)-1):
                if right[i] <= right[i+1]:
                    return False
        
        return True
