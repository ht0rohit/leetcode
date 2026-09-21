class Solution:
    def smallestPalindrome(self, s: str) -> str:
        n = len(s)
        count = [0] * 26

        for elem in s:
            count[ord(elem) - ord('a')] += 1

        res = [''] * n
        i, j = 0, n - 1
        for x in range(26):
            if count[x] > 1:
                while count[x] > 1:
                    res[i] = chr(x + ord('a'))
                    res[j] = chr(x + ord('a'))
                    i += 1
                    j -= 1
                    count[x] -= 2

        for x in range(26):
            if count[x] == 1:
                res[i] = chr(x + ord('a'))
                break

        return "".join(res)