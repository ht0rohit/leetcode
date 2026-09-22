class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        l = len(row)

        count = 0
        for i in range(l):
            if i % 2 != 0:
                if (row[i] % 2 == 0 and row[i - 1] != row[i] + 1) or (row[i] % 2 != 0 and row[i - 1] != row[i] - 1):
                        count += 1

        return count - 1 if count > 1 else 0