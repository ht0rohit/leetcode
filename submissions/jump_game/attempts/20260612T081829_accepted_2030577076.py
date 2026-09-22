class Solution:
    def canJump(self, nums: List[int]) -> bool:
        l = len(nums)
        if l == 1:
            return True

        i = l - 2
        jump = 1
        while i >= 0:
            if nums[i] >= jump:
                jump = 1
            else:
                jump += 1
            i -= 1

        if jump == 1:
            return True
        return False