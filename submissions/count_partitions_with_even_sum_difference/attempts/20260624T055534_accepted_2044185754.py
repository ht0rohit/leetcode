class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        res = 0
        leftSub = prevLeftSub = rightSub = 0
        summ = sum(nums)
        for i in range(len(nums) - 1):
            leftSub = prevLeftSub + nums[i]
            prevLeftSub = leftSub
            rightSub = summ - leftSub
            if abs(leftSub - rightSub) % 2 == 0:
                res += 1

        return res