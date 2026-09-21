class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        for i in range(1, numRows):
            res.append([])
            for j in range(len(res[-2])):
                if j == 0:
                    res[-1].append(1)
                if j != 0 and j != len(res[-2]):
                    res[-1].append(res[-2][j - 1] + res[-2][j])
                if j == len(res[-2]) - 1:
                    res[-1].append(1)

        return res