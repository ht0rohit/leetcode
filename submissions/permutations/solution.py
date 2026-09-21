class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        def backtrack(first):
            if first == n:
                res.append(nums[:])
                return

            for i in range(first, n):
                nums[first], nums[i] = nums[i], nums[first]

                backtrack(first + 1)

                nums[first], nums[i] = nums[i], nums[first]

        backtrack(0)
        return res