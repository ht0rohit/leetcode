class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        intervals = sorted(intervals, key = lambda x: (x[1], x[0]))

        res = 0
        i = 0
        for j in range(1, n):
            if intervals[j][0] < intervals[i][1]:
                res += 1
            else:
                i = j

        return res