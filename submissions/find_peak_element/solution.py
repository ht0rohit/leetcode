class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)

        l, r = 0, n - 1
        while l <= r:
            mid = l + (r - l) // 2
            lelem = nums[mid - 1] if mid > 0 else float('-inf')
            relem = nums[mid + 1] if mid < n - 1 else float('-inf')

            if nums[mid] > lelem and nums[mid] > relem:
                res = mid
                break
            elif nums[mid] > lelem:
                l = mid + 1
            else:
                r = mid - 1

        return res