class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        res = 0

        lsum, rsum = 0, 0
        for i in range(k):
            lsum += cardPoints[i]

        j = n
        for i in range(k - 1, -2, -1):
            res = max(res, lsum + rsum)
            j -= 1
            lsum -= cardPoints[i]
            rsum += cardPoints[j]


        return res