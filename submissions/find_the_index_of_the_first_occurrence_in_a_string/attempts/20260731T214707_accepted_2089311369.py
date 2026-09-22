class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m = len(haystack)
        n = len(needle)

        i, j = 0, 0
        while i < m:
            if haystack[i] == needle[j]:
                j += 1
                i += 1
            else:
                i = i - j + 1
                j = 0

            if j == n:
                return i - n

        return -1
