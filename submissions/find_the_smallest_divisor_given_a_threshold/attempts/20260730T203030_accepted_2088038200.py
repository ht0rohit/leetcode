class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        n = len(nums)
        nums.sort()

        l, r = 1, nums[n-1]
        while l < r:
            mid = l + (r - l) // 2
            th = 0
            for elem in nums:
                th += math.ceil(elem / mid)

            if th > threshold:
                l = mid + 1
            else:
                r = mid

        return l