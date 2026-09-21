class Solution:
    def minimumSwaps(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0

        count = 0
        i, j = 0, n - 1
        while j < n and i < j:
            while i < j and nums[i] != 0:
                i += 1

            while j > i and nums[j] == 0:
                j -= 1

            if j > i:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
                count += 1

        return count