# Runtime: 56 ms, faster than 76.40% of Python3 online submissions for Mean of Array After Removing Some Elements.
# Memory Usage: 14.5 MB, less than 39.21% of Python3 online submissions for Mean of Array After Removing Some Elements.

class Solution:
    def trimMean(self, arr: List[int]) -> float:
        fivepercent = int(len(arr) * 0.05)

        return round(sum(sorted(arr)[fivepercent:-fivepercent]) / (len(arr) - 2*fivepercent), 5)
