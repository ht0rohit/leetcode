class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)

        minv = [-1] * n
        mini = n - 1
        for i in range(n - 1, -1, -1):
            if nums[i] < nums[mini]:
                mini = i
            minv[i] = mini

        print(minv)

        maxi = 0
        for i in range(n):
            if nums[i] > nums[maxi]:
                maxi = i
            score = nums[maxi] - nums[minv[i]]
            if score <= k:
                return i

        return -1
