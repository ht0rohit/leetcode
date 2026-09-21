class Solution:
    def makeFancyString(self, s: str) -> str:
        res = s[:2]
        for i in range(2, len(s)):
            if s[i] == s[i-1] and s[i] == s[i-2]:
                pass
            else:
                res += s[i]
        return res