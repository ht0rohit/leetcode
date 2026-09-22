class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        oddLength = []
        elem = 1
        while elem <= len(arr):
            oddLength.append(elem)
            elem += 2

        summ = 0
        for elem in oddLength:
            i, j = 0, elem
            while j <= len(arr):
                summ += sum(arr[i:j])
                i +=1
                j += 1

        return summ