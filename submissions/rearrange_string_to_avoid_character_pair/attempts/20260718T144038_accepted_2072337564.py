class Solution:
    def rearrangeString(self, s: str, x: str, y: str) -> str:
        if x not in s or y not in s:
            return s

        ycount = 0
        res = ''
        for elem in s:
            if elem == y:
                ycount +=1
            else:
               res += elem

        res = y * ycount + res
        return res