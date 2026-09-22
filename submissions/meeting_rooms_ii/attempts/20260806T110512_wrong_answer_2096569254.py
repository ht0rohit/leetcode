class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        hmap = {}
        for start, end in intervals:
            hmap[start] = 'start'
            hmap[end] = 'end'

        sorted_dict = dict(sorted(hmap.items()))

        rooms, free = 0, 0
        for k, v in sorted_dict.items():
            if v == 'start':
                if not free:
                    rooms += 1
                else:
                    free -= 1
            else:
                free += 1

        return rooms
