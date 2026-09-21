class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        ones = sum(nums)
        
        i, j = 0, 0
        num_ones, max_ones = 0, 0
        
        while i < n:
            num_ones += nums[j % n]
            
            if j - i + 1 < ones:
                j += 1
                continue

            max_ones = max(max_ones, num_ones)
            num_ones -= nums[i]

            i += 1
            j += 1

        
        return ones - max_ones