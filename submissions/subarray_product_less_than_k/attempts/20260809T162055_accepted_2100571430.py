class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        n = len(nums)

        pprod, res = 1, 0
        i, j = 0, 0
        while j < n:
            pprod *= nums[j]
            
            while pprod >= k and i <= j:
                pprod //= nums[i]
                i += 1

            res += (j - i + 1)
            j += 1

        return res