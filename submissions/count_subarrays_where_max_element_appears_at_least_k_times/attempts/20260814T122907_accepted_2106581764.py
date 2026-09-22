class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        m = max(nums)

        i = 0
        res, num_m = 0, 0
        for j in range(n):
            
            if nums[j] == m:
                num_m += 1

            while num_m == k:
                if nums[i] == m:
                    num_m -= 1
                i += 1
            
            res += i

        return res