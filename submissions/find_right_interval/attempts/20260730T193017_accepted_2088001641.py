class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        hmap = {}
        for i, elem in enumerate(intervals):
            hmap[tuple(elem)] = i

        n = len(intervals)
        intervals.sort()
        res = [None] * n

        for i, elem in enumerate(intervals):
            i_org = hmap[tuple(elem)]

            l, r = i, n - 1
            while l < r:
                mid = l + (r - l) // 2

                if intervals[mid][0] >= elem[1]:
                    r = mid
                else:
                    l = mid + 1

            if intervals[l][0] >= elem[1]:
                res[i_org] = hmap[tuple(intervals[l])]
            else:
                res[i_org] = -1

        return res