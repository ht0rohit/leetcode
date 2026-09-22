class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        len_matrix = m * n
        left = 0
        right = len_matrix - 1
        res = False

        while left <= right:
            mid = (left + right) // 2
            x = (mid + 1) // n
            y = (mid + 1) - (((mid + 1) // n) * n)
            if matrix[x][y] == target:
                res = True
                return res
            elif matrix[x][y] > target:
                right = mid - 1
            elif matrix[x][y] < target:
                left = mid + 1
        
        return res
