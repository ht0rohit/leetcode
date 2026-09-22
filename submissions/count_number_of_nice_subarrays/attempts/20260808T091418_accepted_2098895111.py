class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        psum = [0] * (n + 1)

        for i in range(n):
            if nums[i] % 2 == 0:
                psum[i+1] = psum[i]
            else:
                psum[i+1] = psum[i] + 1

        hmap = Counter(psum)

        res = 0
        lastInd = 0
        for i in range(1, n+1):
            if psum[i] != psum[i-1] and psum[i] + k - 1 in hmap:
                res += ((i - lastInd) * hmap[psum[i] + k - 1])
                lastInd = i

        return res
        