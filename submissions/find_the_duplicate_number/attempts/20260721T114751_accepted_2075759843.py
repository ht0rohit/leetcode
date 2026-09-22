class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        res = -1
        i = 0
        while True:
            if nums[abs(nums[i])] < 0:
                res = abs(nums[i])
                break

            nums[abs(nums[i])] = - nums[abs(nums[i])]
            i = abs(nums[i])

        for i in range(len(nums)):
            nums[i] = abs(nums[i])

        return res