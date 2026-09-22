class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        s = sum(weights)

        l, r = max(weights), s
        while l < r:
            mid = l + (r - l) // 2

            w, d = 0, 0
            for elem in weights:
                if w + elem <= mid:
                    w += elem
                else:
                    d += 1
                    w = elem
            else:
                if w != 0:
                    d += 1

            if d <= days:
                r = mid
            else:
                l = mid + 1

        return l