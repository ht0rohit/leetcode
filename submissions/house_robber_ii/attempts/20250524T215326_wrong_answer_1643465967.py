class Solution:
    def rob(self, nums: List[int]) -> int:
        money = [0] * len(nums)
        money[0] = nums[0]

        if len(nums) > 1:
            money[1] = nums[1]
        if len(nums) > 2:
            if len(nums) == 3:
                money[2] = nums[2]
            else:
                money[2] = nums[0] + nums[2]
        
        for i in range(3, len(nums)):
            if i % 2 == 0:
                money[i] = money[i-3] + nums[i]
            else:
                money[i] = money[i-2] + nums[i]

        return max(money)
