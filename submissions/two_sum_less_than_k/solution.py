class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort()

        left, right = 0, len(nums) - 1
        ans = -1

        while left < right:
            curr = nums[left] + nums[right]

            if curr < k:
                ans = max(ans, curr)
                left += 1
            else:
                right -= 1

        return ans
