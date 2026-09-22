class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        grid = [elem for lis in grid for elem in lis]
        grid_set = sorted(list(set(grid)))
        n = len(grid_set)
        
        me1, me2 = n//2, -1
        if n%2 == 0:
            me2 = n//2 - 1

        n1, n2 = 0, 0
        for elem in grid:
            if elem < x:
                y = (grid_set[me1] - elem)/x
            elif elem > x:
                y = (elem - grid_set[me1])/x
            elif elem == x:
                y = (grid_set[me1] - elem)/x
            if y.is_integer():
                n1 += abs(y)
            else:
                return -1

        if me2!=-1:
            for elem in grid:
                if elem < x:
                    y = (grid_set[me2] - elem)/x
                elif elem > x:
                    y = (elem - grid_set[me2])/x
                elif elem == x:
                    y = (grid_set[me2] - elem)/x
                if y.is_integer():
                    n2 += abs(y)
                else:
                    return -1

            return int(min(n1, n2))
        else:
            return int(n1)