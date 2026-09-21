class Solution:
    def check(self, nums: List[int]) -> bool:
        l = len(nums)
        flag = 0
        for i in range(l):
            if nums[i] > nums[(i + 1) % l]:
                if not flag:
                    flag = 1
                else:
                    return False
        
        return True
            