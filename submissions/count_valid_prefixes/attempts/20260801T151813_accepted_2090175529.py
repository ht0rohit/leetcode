class Solution:
    def countValidPrefixes(self, s: str) -> int:
        n = len(s)
        res = 0
        
        num0, num1 = 0, 0
        for i in range(n):
            if s[i] == '0':
                num0 += 1
            else:
                num1 += 1

            if abs(num0 - num1) <= 1:
                res += 1

        return res