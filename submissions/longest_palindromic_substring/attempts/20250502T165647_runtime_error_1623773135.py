class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def checkPal(str, low, high):
            while low < high:
                if str[low] != str[high]:
                    return False
                low += 1
                high -= 1
            return True

        n = len(s)
        maxLen = 1

        for i in range(n):
            for j in range(i, n):
                if checkPal(s, i, j) and (j - i + 1) > maxLen:
                    start = i
                    maxLen = j - i + 1

        return s[start:start + maxLen]