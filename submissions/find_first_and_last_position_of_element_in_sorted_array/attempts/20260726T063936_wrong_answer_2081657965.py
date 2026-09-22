class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = len(nums)
        res = [-1, -1]

        def helper(ind):
            i, j = 0, l - 1
            while i <= j:
                mid = i + (j - i) // 2
                if nums[mid] == target:
                    if ind:
                        if nums[mid + 1] == target:
                            i = mid + 1
                        else:
                            return mid
                    else:
                        if nums[mid - 1] == target:
                            j = mid - 1
                        else:
                            return mid
                elif nums[mid] > target:
                    j = mid - 1
                else:
                    i = mid + 1

            return -1

        res[0] = helper(0)
        if res[0] == -1:
            return [-1, -1]
        res[1] = helper(-1)

        return res
