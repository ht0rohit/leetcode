class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        runningSum = []
        runningSum.append(nums[0])
        for i in range(1, len(nums)):
            runningSum.append(runningSum[i-1] + nums[i])

        return runningSum