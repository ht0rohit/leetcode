class Solution:
    def pivotInteger(self, n: int) -> int:
        summ = (n * (n + 1)) / 2
        leftSum = prevLeftSum = 0
        rightSum = summ

        for i in range(1, n + 1):
            leftSum = prevLeftSum + i
            prevLeftSum = leftSum
            rightSum = rightSum - (i - 1)
            if leftSum == rightSum:
                return i
        else:
            return -1