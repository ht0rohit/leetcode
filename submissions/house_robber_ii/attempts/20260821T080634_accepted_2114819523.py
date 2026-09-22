class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        
        if n == 1:
            return nums[0]
        elif n == 2:
            return max(nums[0], nums[1])

        def max_amount(nums):
            last, prev = nums[0], max(nums[0], nums[1])
            for elem in nums[2:]:
                temp = last
                last = prev
                prev = max(prev, temp + elem)

            return prev
        
        return max(max_amount(nums[:n-1]), max_amount(nums[1:]))