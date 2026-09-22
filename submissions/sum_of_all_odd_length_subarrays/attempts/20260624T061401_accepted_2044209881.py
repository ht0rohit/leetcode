class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        oddLength = []
        elem = 1
        while elem <= len(arr):
            oddLength.append(elem)
            elem += 2

        summ = 0
        for i in range(len(arr)):
            sum_i = 0
            for elem in oddLength:
                j = i + elem
                if j < len(arr) + 1:
                    if j - i > 1:
                        sum_i = sum_i + arr[j-1] + arr[j-2]
                    else:
                        sum_i = sum_i + arr[j-1]
                    summ += sum_i

        return summ