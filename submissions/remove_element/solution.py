class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = len(nums)

        i, j = 0, l - 1
        while j >= 0 and nums[j] == val:
            j -= 1

        while i <= j:
            if nums[i] == val:
                nums[i], nums[j] = nums[j], nums[i]
                j -= 1

            i += 1
            while j >= i and nums[j] == val:
                j -= 1

        return j + 1