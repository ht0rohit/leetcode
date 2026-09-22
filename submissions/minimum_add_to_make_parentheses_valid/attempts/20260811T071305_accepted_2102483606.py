class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        lb = 0
        res = 0

        for elem in s:
            if elem == '(':
                lb += 1
            elif elem == ')':
                if lb:
                    lb -= 1
                else:
                    res += 1

        return res + lb