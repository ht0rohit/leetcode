class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n == 0 or n == 1:
            return 0

        nums.sort()
        count = 0

        for i in range(n-2):
            lo, hi = i + 1, n - 1
            
            while lo < hi:
                cursum = nums[i] + nums[lo] + nums[hi]
                if cursum < target:
                    count += hi - lo
                    lo += 1
                else:
                    hi -= 1

        return count
