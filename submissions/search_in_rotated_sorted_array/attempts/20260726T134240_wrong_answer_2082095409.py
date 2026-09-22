class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = len(nums)

        i, j = 0, l - 1
        while i <= j:
            mid = i + (j - i) // 2

            if nums[mid] == target:
                return mid

            # Left half is sorted
            if nums[i] < nums[mid]:
                if nums[i] <= target < nums[mid]:
                    j = mid - 1
                else:
                    i = mid + 1

            # Right half is sorted
            else:
                if nums[mid] < target <= nums[j]:
                    i = mid + 1
                else:
                    j = mid - 1

        return - 1