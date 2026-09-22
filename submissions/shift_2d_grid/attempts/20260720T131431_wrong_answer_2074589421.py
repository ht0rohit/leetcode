class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        l = m * n
        i, j = 0, 0
        source = [i, j]
        temp1 = grid[i][j]
        it  = 0

        while it < l:
            i = (i + (j + k) // n) % n
            j = ((j + k) % n) % n

            temp2 = grid[i][j]
            grid[i][j] = temp1
            temp1 = temp2

            it += 1
            if [i, j] == source and it < l:
                i = (i + (j + 1) // n) % n 
                j = ((j + 1) % n) % n
                source = [i, j]
                temp1 = grid[i][j]

        return grid
