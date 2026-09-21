class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        lrange, hrange = 1, max(piles)

        l, r = lrange, hrange
        while l < r:
            mid = l + (r - l) // 2

            t = 0
            for elem in piles:
                t += math.ceil(elem / mid)

            if t <= h:
                r = mid
            else:
                l = mid + 1

        return l
