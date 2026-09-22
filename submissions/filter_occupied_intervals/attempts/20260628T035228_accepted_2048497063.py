class Solution:
    def filterOccupiedIntervals(self, occupiedIntervals: List[List[int]], freeStart: int, freeEnd: int) -> List[List[int]]:
        occupiedIntervals.sort()

        mergedIntervals = []

        for intervalStart, intervalEnd in occupiedIntervals:
            if not mergedIntervals or intervalStart > mergedIntervals[-1][1] + 1:
                mergedIntervals.append([intervalStart, intervalEnd])
            else:
                if intervalEnd > mergedIntervals[-1][1]:
                    mergedIntervals[-1][1] = intervalEnd

        remainingIntervals = []

        for occupiedStart, occupiedEnd in mergedIntervals:
            if occupiedEnd < freeStart or occupiedStart > freeEnd:
                remainingIntervals.append([occupiedStart, occupiedEnd])
            else:
                if occupiedStart < freeStart:
                    remainingIntervals.append([occupiedStart, freeStart - 1])

                if occupiedEnd > freeEnd:
                    remainingIntervals.append([freeEnd + 1, occupiedEnd])

        return remainingIntervals