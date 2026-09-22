class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)

        l, r = 0, n - 1
        while l < r:
            mid = l + (r - l) // 2

            if mid % 2 == 0:
                if nums[mid] == nums[mid - 1]:
                    r = mid - 1
                elif nums[mid] == nums[mid + 1]:
                    l = mid + 1
                else:
                    return nums[mid]
            else:
                if nums[mid] == nums[mid - 1]:
                    l = mid + 1
                elif nums[mid] == nums[mid + 1]:
                    r = mid - 1
                else:
                    return nums[mid]

        return nums[l]