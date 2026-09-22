class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows, columns = [], []
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows += [i]
                    columns += [j]

        for elem in rows:
            matrix[elem] = [0]*n
        for elem in columns:
            for i in range(m):
                matrix[i][elem] = 0

        return matrix