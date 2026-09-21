class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        clsum = nums[0] + nums[1] + nums[n - 1]

        for i in range(n-2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            lo, hi = i + 1, n - 1
            
            while lo < hi:
                cursum = nums[i] + nums[lo] + nums[hi]
                clsum = cursum if abs(target - clsum) > abs(target - cursum) else clsum

                if cursum == target:
                    return cursum
                elif cursum < target:
                    lo += 1
                elif cursum > target:
                    hi -= 1

        return clsum
