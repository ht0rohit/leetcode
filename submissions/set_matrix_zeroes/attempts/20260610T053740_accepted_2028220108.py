class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row_i, col_i = [], []
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row_i += [i]
                    col_i += [j]

        for elem in row_i:
            for i in range(n):
                matrix[elem][i] = 0

        for elem in col_i:
            for i in range(m):
                matrix[i][elem] = 0
        