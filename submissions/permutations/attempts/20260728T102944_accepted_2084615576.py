class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        used = [False] * n
        curr, res = [], []

        def backtrack(i):
            if i == n:
                res.append(curr[:])
                return

            for x in range(n):
                if used[x]:
                    continue
                curr.append(nums[x])
                used[x] = True
                backtrack(i + 1)
                curr.pop()
                used[x] = False

        i = 0
        backtrack(i)

        return res