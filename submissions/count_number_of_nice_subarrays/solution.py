class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        for i in range(n):
            if nums[i] % 2 == 0:
                nums[i] = 0
            else:
                nums[i] = 1

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

        return atMost(k) - atMost(k - 1)