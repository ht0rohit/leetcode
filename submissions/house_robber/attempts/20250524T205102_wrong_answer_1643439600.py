class Solution:
    def rob(self, nums: List[int]) -> int:
        money_even_houses = 0
        for i in range(0, len(nums), 2):
            money_even_houses += nums[i]
        money_odd_houses = 0
        for i in range(1, len(nums), 2):
            money_odd_houses += nums[i]
        
        return max(money_even_houses, money_odd_houses)