class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        hmap = {}

        psum = 0
        res = 0
        for i in range(n):
            psum += nums[i]
            if psum == k:
                res += 1
            else:
                if psum - k in hmap:
                    res += hmap[psum-k]

            hmap[psum] = hmap.get(psum, 0) + 1

        return res