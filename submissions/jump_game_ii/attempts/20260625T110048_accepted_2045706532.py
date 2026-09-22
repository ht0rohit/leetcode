class Solution:
    def jump(self, nums: List[int]) -> int:
        l = len(nums)
        if l == 1:
            return 0

        jumps = [0] * len(nums)
        i, j = 0, 1
        for i in range(l):
            while j <= (i + nums[i]) and j < l:
                jumps[j] = jumps[i] + 1
                j += 1

        return jumps[-1]