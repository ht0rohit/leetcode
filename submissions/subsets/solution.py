class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        curr, res = [], []

        def gen_subset(i):
            if i == n:
                res.append(curr[:])
                return

            curr.append(nums[i])
            gen_subset(i + 1)
            curr.pop()
            gen_subset(i + 1)

        i = 0
        gen_subset(i)

        return res