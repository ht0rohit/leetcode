class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        n = len(nums)
        nums.sort()

        l, r = nums[0], nums[n-1]
        maxD = nums[0]

        while l <= r:
            mid = l + (r - l) // 2
            th = 0
            for elem in nums:
                th += math.ceil(elem / mid)

            if th == threshold:
                return mid
            elif th > threshold:
                l = mid + 1
            else:
                r = mid - 1

        return l