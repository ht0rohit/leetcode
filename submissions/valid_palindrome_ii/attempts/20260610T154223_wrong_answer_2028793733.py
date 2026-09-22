class Solution:
    def validPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        count = 0

        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            elif i+1 < j and s[i+1] == s[j] and count == 0:
                i += 2
                j -= 1
                count += 1
            elif i < j-1 and s[i] == s[j-1] and count == 0:
                i += 1
                j -= 2
                count += 1
            elif (i+1 >= j or i >= j-1) and count == 0:
                i += 1
                j -= 1
            else:
                return False
        else:
            return True