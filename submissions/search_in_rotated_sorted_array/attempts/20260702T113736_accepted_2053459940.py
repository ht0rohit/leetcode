class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = len(nums)

        s_ind = -1
        for i in range(l - 1):
            if nums[i] > nums[i+1]:
                s_ind = i
                break

        i, j = 0, l - 1
        while i <= j:
            mid_temp = (i + j) // 2
            mid = (mid_temp + s_ind + 1) % l
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                j = mid_temp - 1
            else:
                i = mid_temp + 1

        return - 1