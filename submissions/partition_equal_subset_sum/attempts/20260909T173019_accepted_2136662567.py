class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        subsum = sum(nums)
        if subsum % 2 != 0:
            return False
        eqsum = subsum // 2

        @cache
        def backt(i, cursum):
            if i >= n or cursum > eqsum:
                return False
            elif cursum == eqsum:
                return True

            cursum += nums[i]
            if not backt(i + 1, cursum):
                cursum -= nums[i]
                return backt(i + 1, cursum)

            return True


        return backt(0, 0)