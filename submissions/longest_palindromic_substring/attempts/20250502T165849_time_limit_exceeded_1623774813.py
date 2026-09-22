class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def check_palindrome(str, low, high):
            while low < high:
                if str[low] != str[high]:
                    return False
                low += 1
                high -= 1
            return True

        n, maxLen, start = len(s), 1, 0

        for i in range(n):
            for j in range(i, n):
                if check_palindrome(s, i, j) and (j - i + 1) > maxLen:
                    start = i
                    maxLen = j - i + 1

        return s[start:start + maxLen]