class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        lo, hi = min(nums), max(nums)
        psum = [0] * (hi - lo + 1)
        for num in nums:
            psum[num - lo] += num

        prev2 = prev1 = 0
        for num in psum:
            prev2, prev1 = prev1, max(prev1, prev2 + num)

        return prev1