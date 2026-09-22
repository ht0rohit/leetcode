class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.m, self.n = len(matrix), len(matrix[0])

        for i in range(1, self.m):
            self.matrix[i][0] += self.matrix[i-1][0]
        for j in range(1, self.n):
            self.matrix[0][j] += self.matrix[0][j-1]

        for i in range(1, self.m):
            for j in range(1, self.n):
                self.matrix[i][j] = self.matrix[i][j] + self.matrix[i-1][j] + self.matrix[i][j-1] - self.matrix[i-1][j-1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if row1 == 0 and col1 == 0:
            res = self.matrix[row2][col2]
        elif row1 == 0:
            res = self.matrix[row2][col2] - self.matrix[row1][col1-1]
        elif col1 == 0:
            res = self.matrix[row2][col2] - self.matrix[row1-1][col1]
        else:
            res = self.matrix[row2][col2] + self.matrix[row1-1][col1-1] - self.matrix[row1-1][col2] - self.matrix[row2][col1-1]
        
        return res


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)