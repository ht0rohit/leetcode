class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        nums.sort()
        res = []
        
        for i in range(n-2):
            lo, hi = i + 1, n - 1
            
            while lo < hi:
                summ = nums[i] + nums[lo] + nums[hi]
                if summ == 0:
                    res.append([nums[i], nums[lo], nums[hi]])
                    break
                if summ < 0:
                    lo += 1
                elif summ > 0:
                    hi -= 1

        return res

             
