class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        contSum = sum(nums[:k])

        maxAvg = round(contSum / k, 5)
        for i in range(1, n - k + 1):
            contSum = contSum - nums[i-1] + nums[i+k-1]
            avg = round(contSum / k, 5)
            maxAvg = max(maxAvg, avg)

        return maxAvg
