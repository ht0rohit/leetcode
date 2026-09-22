class Solution:
    def brightestPosition(self, lights: List[List[int]]) -> int:
        m = len(lights)
        shift = lights[0][0]
        n = shift + lights[0][1]
        
        for i in range(m):
            centre = lights[i][0]
            lights[i][0] = centre - lights[i][1]
            lights[i][1] += centre
            shift = min(shift, lights[i][0])
            n = max(n, lights[i][1])
        
        n = n - shift + 1
        brightest = [0] * n

        for l, r in lights:
            brightest[l - shift] += 1
            if r + 1 - shift < n:
                brightest[r + 1 - shift] -= 1

        bpos = 0
        for i in range(1, n):
            brightest[i] += brightest[i - 1]
            if brightest[i] > brightest[bpos]:
                bpos = i

        return bpos + shift