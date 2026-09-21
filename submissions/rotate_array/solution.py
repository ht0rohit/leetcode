class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        i, start, it = 0, 0, 0
        temp1 = nums[0]

        while it < l:
            temp2 = nums[(i + k) % l]
            nums[(i + k) % l] = temp1
            temp1 = temp2
            i = (i + k) % l
            it += 1
            if i == start and it < l:
                i += 1
                start = i
                temp1 = nums[i]

        return nums