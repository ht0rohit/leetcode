class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        if n == 1:
            return intervals

        intervals.sort()

        res = []
        i = 0
        elem = intervals[i]
        for j in range(1, n):
            if elem[1] >= intervals[j][0]:
                elem = [elem[0], max(elem[1], intervals[j][1])]
            else:
                res.append(elem)
                i = j
                elem = intervals[i]

        res.append(elem)

        return res
