class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        res = ""
        i, start_index = 0, 0
        while i < len(s):
            if s[i] == " ":
                res = s[start_index:i] + " " + res
                while s[i] == " ":
                    i += 1
                start_index = i
            elif i == len(s)-1:
                res = s[start_index:i+1] + " " + res
                i += 1
            else:
                i += 1
        return res.strip()