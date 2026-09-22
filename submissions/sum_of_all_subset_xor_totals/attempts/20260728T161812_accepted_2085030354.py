class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        
        n = len(nums)
        res = []

        def gen_subset(i, curr):
            if i == n:
                res.append(curr)
                return

            temp = curr
            curr ^= nums[i]
            gen_subset(i + 1, curr)
            gen_subset(i + 1, temp)

        i = 0
        curr = 0
        gen_subset(i, curr)

        return sum(res)