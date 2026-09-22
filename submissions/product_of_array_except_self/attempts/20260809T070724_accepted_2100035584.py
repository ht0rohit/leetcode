class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        psum = [1] * (n + 1)
        psum[n-1] = nums[n-1]
        for i in range(n-2, -1, -1):
            psum[i] = psum[i+1] * nums[i]

        res = [0] * n
        res[0] = psum[1]
        mul = 1
        for i in range(1, n):
            mul *= nums[i-1]
            res[i] = psum[i+1] * mul

        return res