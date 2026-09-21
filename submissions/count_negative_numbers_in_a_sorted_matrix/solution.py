class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        res = 0
        j = n - 1
        for i in range(m):
            while j >= 0 and grid[i][j] < 0:
                j -= 1
            res += n - 1 - j

        return res