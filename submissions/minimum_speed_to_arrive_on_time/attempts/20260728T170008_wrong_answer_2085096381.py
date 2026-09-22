class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        n = len(dist)

        d = sum(dist)
        s = math.ceil(d / hour)

        t = 0
        for i in range(n):
            if i == n - 1:
                temp = round(dist[i] / s, 2)
                t += temp
                break
            temp = math.ceil(dist[i] / s)
            t += temp

        return s if t <= hour else -1

