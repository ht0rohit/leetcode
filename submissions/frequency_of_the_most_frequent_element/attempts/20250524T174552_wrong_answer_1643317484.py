class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        frequent_elem = [None]*len(nums)
        frequent_elem[0] = 0

        for i in range(1, len(nums)):
            frequent_elem[i] = nums[i] - nums[i-1]
        
        for i in range(1, len(nums)):
            frequent_elem[i] = frequent_elem[i] + frequent_elem[i-1]

        for i in range(1, len(nums)):
            frequent_elem[i] = frequent_elem[i] + frequent_elem[i-1]

        for i in range(len(nums)):
            if frequent_elem[i] > k:
                return i
            if i == len(nums) - 1:
                return i + 1

# 1, 2, 4 // 5
# 0, 1, 2
# 0, 1, 3
# 0, 1, 4
# 1
# 3, 2

# 1, 4, 8, 13 // 5
# 0, 3, 4, 5
# 0, 3, 7, 13
# 0, 3, 10, 20
# 3
# 7 4
# 12 9 5

# 1, 2, 3, 4, 5, 7, 9, 10, 12 // 8
# 0, 1, 1, 1, 1, 2, 2, 1, 2
# 0, 1, 2, 3, 4, 6, 8, 9, 11
# 0, 1, 3, 6, 10, 16, 24, 33, 44

# 3, 9, 6 // 2
# 0, 6, -3
# 0, 6, 3
# 0, 6, 9