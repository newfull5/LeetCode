# Runtime: 88 ms, faster than 57.05% of Python3 online submissions for Merge Intervals.
# Memory Usage: 16 MB, less than 85.38% of Python3 online submissions for Merge Intervals.

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key = lambda x: x[-1])

        while True:
            temp = []
            prev = intervals[:]

            while len(intervals) >= 2:
                b = intervals.pop()
                a = intervals.pop()

                if a[1] >= b[0]:
                    intervals.append([min(a[0],b[0]), b[1]])
                else:
                    temp.append(b)
                    intervals.append(a)

            intervals += temp
            intervals = sorted(intervals, key = lambda x: x[-1])

            if prev == intervals:
                break
                
        return intervals
