class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        for i in range(n):
            if nums[i] % 2 == 0:
                nums[i] = 0
            else:
                nums[i] = 1

        hmap = {}
        res, psum = 0, 0
        for i in range(n):
            psum += nums[i]

            if psum == k:
                res += 1
            
            res += hmap.get(psum - k, 0)

            hmap[psum] = hmap.get(psum, 0) + 1

        return res
        