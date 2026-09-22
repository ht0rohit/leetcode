class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        n = len(nums)

        def atMost(goal):
            if goal < 0:
                return 0

            res = 0
            i = 0
            csum = 0

            for j in range(len(nums)):
                csum += nums[j]

                while csum > goal:
                    csum -= nums[i]
                    i += 1

                res += j - i + 1

            return res

        return atMost(goal) - atMost(goal - 1)