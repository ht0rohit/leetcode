class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        if n == 1:
            return 0

        intervals.sort()

        res = 0
        i = 0
        for j in range(1, n):
            if intervals[i][1] > intervals[j][0]:
                res += 1
            else:
                i = j

        return res