class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)

        i, j = 0, 0
        csum = nums[0]
        mlen = n + 1

        while j < n:
            if csum >= target:
                clen = j - i + 1
                mlen = min(mlen, clen)
                csum -= nums[i]
                i += 1
            else:
                j += 1
                if j < n:
                    csum += nums[j]

        return mlen if mlen != n + 1 else 0