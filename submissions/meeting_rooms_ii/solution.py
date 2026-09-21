class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        
        start, end = [], []
        for s, e in intervals:
            start.append(s)
            end.append(e)
        start.sort()
        end.sort()

        i, j = 0, 0
        rooms, free = 0, 0
        while i < n:
            if start[i] < end[j]:
                if not free:
                    rooms += 1
                else:
                    free -= 1
                i += 1
            elif start[i] > end[j]:
                free += 1
                j += 1
            else:
                i += 1
                j += 1

        return rooms