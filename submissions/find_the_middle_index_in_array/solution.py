class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        summ = sum(nums)
        leftSum = prevLeftSum = 0
        rightSum = summ - nums[0]

        if int(leftSum) == int(rightSum):
            return 0

        for i in range(1, len(nums)):
            leftSum = prevLeftSum + nums[i - 1]
            prevLeftSum = leftSum
            rightSum = rightSum - nums[i]
            print(int(leftSum), int(rightSum))
            if int(leftSum) == int(rightSum):
                return i
        else:
            return -1