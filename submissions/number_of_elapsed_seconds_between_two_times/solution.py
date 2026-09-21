class Solution:
    def secondsBetweenTimes(self, startTime: str, endTime: str) -> int:
        startTime = startTime.split(':')
        startTime = [int(elem) for elem in startTime]

        endTime = endTime.split(':')
        endTime = [int(elem) for elem in endTime]

        l = len(endTime)

        start = 0
        end = 0
        c = 0

        for i in range(l - 1, -1, -1):
            start += startTime[i] * (60 ** c)
            end += endTime[i] * (60 ** c)
            c += 1

        return end - start