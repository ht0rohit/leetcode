class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        total_sum = n * (n + 1) // 2
        count_div = n // m
        sum_div = m * count_div * (count_div + 1) // 2
        return total_sum - 2 * sum_div