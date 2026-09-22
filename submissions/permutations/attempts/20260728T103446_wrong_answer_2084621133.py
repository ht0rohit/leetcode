class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        res.append(nums[:])

        for i in range(n):
            x = n - 1
            if i == n - 1:
                x = n - 2
            for j in range(x):
                nums[j], nums[j+1] = nums[j+1], nums[j]
                res.append(nums[:])

        return res