class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        firstRow = "." + "#" * (n - 1)
        path = [firstRow] * (m - 1)
        lastRow = "." * n
        path += [lastRow]
        return path