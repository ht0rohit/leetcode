class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort(reverse=True)
        
        res = 0
        for i in range(n):
            j = i
            curr, diff = 0, 0
            while j < n:
                diff += nums[i] - nums[j]
                if diff <= k:
                    curr += 1
                    res = max(res, curr)
                    j += 1
                else:
                    break

        return res
