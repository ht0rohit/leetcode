class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        temp = str(num)
        l = len(temp)

        res = 0
        for i in range(0, l - k + 1):
            if int(temp[i: i + k]) and num % int(temp[i: i + k]) == 0:
                res += 1

        return res