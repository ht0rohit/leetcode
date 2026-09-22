class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        ind = [0] * n
        count = 0
        for i in range(1, n):
            if abs(nums[i] - nums[i-1]) <= maxDiff:
                ind[i] = count
            else:
                 ind[i] = count + 1
                 count += 1

        return [ind[j] == ind[k] for j, k in queries]
