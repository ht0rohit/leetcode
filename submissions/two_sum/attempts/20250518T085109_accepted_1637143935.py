class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        for i in range(len(nums)):
            if nums[i] not in nums_dict:
                nums_dict[nums[i]] = [i]
            else:
                nums_dict[nums[i]] += [i]

        for i in range(len(nums)):
            remainder = target - nums[i]
            indexes = nums_dict.get(remainder, None)
            if indexes:
                for j in indexes:
                    if i!= j:
                        return i, j
