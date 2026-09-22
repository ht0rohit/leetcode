class Solution:
    def brightestPosition(self, lights: List[List[int]]) -> int:
        n = len(lights)
        for i in range(n):
            centre = lights[i][0]
            lights[i][0] = centre - lights[i][1]
            lights[i][1] += centre

        lights.sort()
        hmap = {}
        
        maxB = [lights[0][0], 1]
        for elem in lights:
            for e in range(elem[0], elem[1] + 1):
                hmap[e] = hmap.get(e, 0) + 1
                if hmap[e] > maxB[1]:
                    maxB = [e, hmap[e]]

        return maxB[0]