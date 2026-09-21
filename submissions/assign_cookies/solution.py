class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        m, n = len(g), len(s)
        g.sort()
        s.sort()

        res = 0
        i, j = 0, 0
        while i < m and j < n:
            if s[j] >= g[i]:
                res += 1
                i += 1
                j += 1
            else:
                j += 1

        return res
