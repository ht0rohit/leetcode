class Solution:
    def validPalindrome(self, s: str) -> bool:
        count = 0

        def valid(i, j):
            nonlocal count

            while i < j:
                if s[i] != s[j]:
                    if count:
                        return False
                    else:
                        count += 1
                        return valid(i + 1, j) or valid(i, j - 1)

                i += 1
                j -= 1

            return True
        
        i, j = 0, len(s) - 1
        return valid(i, j)