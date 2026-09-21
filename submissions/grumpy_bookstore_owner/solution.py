class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers)
        
        gsum = 0
        for i in range(minutes):
            if grumpy[i]:
                gsum += customers[i]

        maxsum = gsum
        l, r = 0, minutes - 1
        j, i = i + 1, 1
        while j < n:
            if grumpy[i - 1]:
                gsum -= customers[i - 1]
            if grumpy[j]:
                gsum += customers[j]

            if gsum > maxsum:
                l, r = i, j
                maxsum = gsum

            i += 1
            j += 1

        res = 0
        for i in range(n):
            if not grumpy[i] or (grumpy[i] and l <= i <= r):
                res += customers[i]

        return res