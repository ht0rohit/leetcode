class Solution:
    def brightestPosition(self, lights: List[List[int]]) -> int:
        n = len(lights)
        hmap = {}

        maxB = [-1, 0]
        for elem in lights:
            for e in range(elem[0] - elem[1], elem[0] + elem[1] + 1):
                hmap[e] = hmap.get(e, 0) + 1
                if hmap[e] > maxB[1]:
                    maxB = [e, hmap[e]]

        return maxB[0]