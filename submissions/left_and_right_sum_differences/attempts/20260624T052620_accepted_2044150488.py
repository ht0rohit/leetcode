class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        summ = sum(nums)
        answer, leftSum, rightSum = [0] * len(nums), [0] * len(nums), [summ] * len(nums)

        for i in range(len(nums)):
            if i == 0:
                leftSum[i] = 0
            else:
                leftSum[i] = leftSum[i-1] + nums[i-1]

            if i == len(nums) - 1:
                rightSum[i] = 0
            else:
                rightSum[i] = rightSum[i-1] - nums[i]

        for i in range(len(nums)):
            answer[i] = abs(leftSum[i] - rightSum[i])

        return answer
