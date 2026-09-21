class Solution:
    def maxValidPairSum(self, nums: list[int], k: int) -> int:
        
        best_left = nums[0]
        ans = min(nums) - 1

        for j in range(k, len(nums)):
            best_left = max(best_left, nums[j - k])
            ans = max(ans, best_left + nums[j])

        return ans