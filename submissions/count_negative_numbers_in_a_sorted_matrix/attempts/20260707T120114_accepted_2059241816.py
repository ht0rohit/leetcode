class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        l = len(grid[0])
        
        res = 0
        for row in grid:
            i, j = 0, l - 1
            while i <= j:
                mid = i + (j - i) // 2
                if row[mid] < 0:
                    j = mid - 1
                else:
                    i = mid + 1
            
            res += (l - i)
        
        return res