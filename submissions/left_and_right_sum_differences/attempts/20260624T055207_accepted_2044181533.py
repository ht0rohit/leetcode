class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        summ = sum(nums)
        answer = []
        leftSum = prevLeftSum = rightSum = 0
        for i in range(len(nums)):
            if i == 0:
                leftSum = prevLeftSum = 0
            else:
                leftSum = prevLeftSum + nums[i-1]
                prevLeftSum = leftSum

            if i == len(nums) - 1:
                rightSum = 0
            else:
                rightSum = summ - leftSum - nums[i]

            answer.append(abs(leftSum - rightSum))

        return answer
