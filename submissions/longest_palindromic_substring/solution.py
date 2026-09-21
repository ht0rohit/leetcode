class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        res = ""

        for i in range(n):
            
            # Odd sequence
            if 1 > len(res):
                res = s[i]
            l, r = i - 1, i + 1
            while l >= 0 and r < n:
                if s[l] == s[r]:
                    if r - l + 1 > len(res):
                        res = s[l: r + 1]
                    l -= 1
                    r += 1
                else:
                    break

            # Even sequence
            if i < n - 1 and s[i] == s[i+1]:
                if 2 > len(res):
                    res = s[i: i + 2]
                l, r = i - 1, i + 2
                while l >= 0 and r < n:
                    if s[l] == s[r]:
                        if r - l + 1 > len(res):
                            res = s[l: r + 1]
                        l -= 1
                        r += 1
                    else:
                        break

        return res