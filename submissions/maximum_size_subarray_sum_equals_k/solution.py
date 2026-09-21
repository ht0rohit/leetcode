class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        n = len(nums)
        hmap = {0: -1}

        psum = 0
        maxsize = 0
        for i in range(n):
            psum += nums[i]
            if psum - k in hmap:
                ind = hmap[psum - k]
                maxsize = max(maxsize, i - ind)

            if psum not in hmap:
                hmap[psum] = i

        return maxsize