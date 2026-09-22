class Solution:
    def check(self, nums: List[int]) -> bool:
        flag = 1
        for i in range(len(nums)):
            if i < len(nums)-1:
                if nums[i+1] >= nums[i]:
                    pass
                elif nums[0] >= nums[len(nums)-1] and flag:
                    flag = 0
                else:
                    break
        else:
            return True

        return False