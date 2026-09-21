class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        summ = sum(nums)
        leftSum = prevLeftSum = 0
        rightSum = summ - nums[0]

        if int(leftSum) == int(rightSum):
            return 0

        for i in range(1, len(nums)):
            leftSum = prevLeftSum + nums[i - 1]
            prevLeftSum = leftSum
            rightSum = rightSum - nums[i]
            if int(leftSum) == int(rightSum):
                return i
        else:
            return -1