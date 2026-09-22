class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = len(nums)

        i, j = 0, l - 1
        while i <= j:
            mid = i + (j - i) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] >= nums[j]:
                if target > nums[j] and target < nums[mid]:
                    j = mid - 1
                else:
                    i = mid + 1
            else:
                if target <= nums[j] and target > nums[mid]:
                    i = mid + 1
                else:
                    j = mid - 1

        return - 1