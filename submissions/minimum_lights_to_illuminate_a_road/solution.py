class Solution:
    def minLights(self, lights: list[int]) -> int:
        n = len(lights)

        illuminated = [0] * n
        reach = -1
        for i in range(n):
            if lights[i] != 0:
                reach = max(reach, i + lights[i])
            if i <= reach:
                illuminated[i] = 1

        reach = n
        for i in range(n - 1, -1, -1):
            if lights[i] != 0:
                reach = min(reach, i - lights[i])
            if i >= reach:
                illuminated[i] = 1

        csum = 0
        res = 0
        for elem in illuminated:        
            if elem:
                res += math.ceil(csum / 3)
                csum = 0
            else:
                csum += 1

        res += math.ceil(csum / 3)

        return res