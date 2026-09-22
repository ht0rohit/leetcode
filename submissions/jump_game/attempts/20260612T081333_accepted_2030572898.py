class Solution:
    def canJump(self, nums: List[int]) -> bool:
        l = len(nums)
        if l == 1:
            return True

        i = l - 2
        condition = 1
        flag = 0
        while i >= 0:
            if nums[i] >= condition:
                flag = 0
                condition = 1
            else:
                flag = 1
                condition += 1
            i -= 1

        if flag:
            return False
        else:
            return True