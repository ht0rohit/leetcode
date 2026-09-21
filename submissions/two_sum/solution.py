class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}
        for i in range(len(nums)):
            if target - nums[i] in indices:
                return [i, indices[target - nums[i]]]
            indices[nums[i]] = i