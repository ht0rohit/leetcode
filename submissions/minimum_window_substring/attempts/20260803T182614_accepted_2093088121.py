class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m, n = len(s), len(t)
        if m < n:
            return ""

        smap = Counter(t)
        distinct = len(smap)
        winmap = {}
        isdist = 0

        res = (0, m)
        i, j = 0, 0
        while j < m:
            winmap[s[j]] = winmap.get(s[j], 0) + 1
            if s[j] in smap and smap[s[j]] == winmap[s[j]]:
                isdist += 1

            while isdist == distinct:
                if j - i + 1 < res[1] - res[0] + 1:
                    res = (i, j)

                winmap[s[i]] -= 1
                if s[i] in smap and winmap[s[i]] < smap[s[i]]:
                    isdist -= 1
                i += 1

            j += 1
        
        if res == (0, m):
            return ""

        return s[res[0]: res[1] + 1]
