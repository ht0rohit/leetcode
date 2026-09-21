class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = len(nums)
        maxelem = nums[0]

        i, j = 1, 1
        while j < l:
            while j + 1 < l and nums[j] <= maxelem:
                j += 1
            if j == l - 1 and nums[j] == maxelem:
                return i
            maxelem = max(maxelem, nums[j])
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j += 1

        return i