class Solution:
    def minLights(self, lights: list[int]) -> int:
        n = len(lights)

        intervals = []
        for i in range(n):
            if lights[i] != 0:
                start = max(0, i - lights[i])
                end = min(n - 1, i + lights[i])
                intervals.append([start, end])

        if not intervals:
            return math.ceil(n / 3)

        intervals.sort()

        merge = []
        i = 0
        elem = intervals[i]
        for j in range(1, len(intervals)):
            if elem[1] >= intervals[j][0]:
                elem = [elem[0], max(elem[1], intervals[j][1])]
            else:
                merge.append(elem)
                i = j
                elem = intervals[i]
        merge.append(elem)

        end = 0
        res = 0
        for elem in merge:
            res += math.ceil((elem[0] - end) / 3)
            end = elem[1]
        res += math.ceil((n - 1 - elem[1]) / 3)

        return res