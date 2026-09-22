class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        missing = len(nums)
        for i, elem in enumerate(nums):
            missing ^= i
            missing ^= elem

        return missing