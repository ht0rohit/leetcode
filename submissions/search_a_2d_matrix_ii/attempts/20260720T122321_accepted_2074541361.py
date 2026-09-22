class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])

        l, r = 0, n - 1
        while l <= r:
            mid = l + (r - l) // 2
            if matrix[0][mid] == target:
                return True
            elif matrix[0][mid] < target:
                l = mid + 1
            elif matrix[0][mid] > target:
                r = mid - 1

        x = l
        for i in range(x):
            l, r = 0, m - 1
            while l <= r:
                mid = l + (r - l) // 2
                if matrix[mid][i] == target:
                    return True
                elif matrix[mid][i] < target:
                    l = mid + 1
                elif matrix[mid][i] > target:
                    r = mid - 1

        return False