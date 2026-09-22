class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k == 0:
            return 0
            
        n = len(nums)
        hmap = {}

        psum = 1
        res = 0
        for i in range(n):
            psum *= nums[i]
            if psum < k:
                res += 1

            target = psum // k
            l, r = 0, len(hmap)
            while l < r:
                mid = l + (r - l) // 2
                if hmap[mid] > target:
                    r = mid
                else:
                    l = mid + 1
            
            if l != len(hmap):
                res += len(hmap) - l

            hmap[i] = psum

        return res
