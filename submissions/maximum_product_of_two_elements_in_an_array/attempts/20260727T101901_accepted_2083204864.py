class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)

        for i in range(n):
            nums[i] *= -1
        heapq.heapify(nums)

        num1 = heapq.heappop(nums)
        num2 = heapq.heappop(nums)
        res = (num1 + 1) * (num2 + 1)

        return res