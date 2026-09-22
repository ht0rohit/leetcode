class Solution:
    def jump(self, nums: List[int]) -> int:
        i, j = 0, 1
        num_jump, len_jump, flag = 0, 0, 0
        
        while j < len(nums):
            init_i = i
            while j <= nums[init_i] + len_jump:
                if nums[j] >= nums[init_i]:
                    flag = 1
                    i = j
                    j += 1
                else:
                    j += 1
            
            num_jump += 1
            if flag:
                len_jump += i - init_i
            else:
                len_jump += nums[i]
                i = j - 1
            j = i + 1
            flag = 0

        return num_jump
