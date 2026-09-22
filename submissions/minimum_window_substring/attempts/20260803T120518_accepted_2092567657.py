class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m, n = len(s), len(t)
        if m < n:
            return ""

        hmap = {}
        for elem in t:
            hmap[elem] = hmap.get(elem, 0) + 1
        temp = hmap.copy()

        i, j = 0, 0
        minWin = ' ' * (m + 1)
        
        while i < m:
            while i < m and j < n:
                if s[i] in temp and temp[s[i]] > 0:
                    temp[s[i]] -= 1
                    i += 1
                    j += 1
                else:
                    i += 1

            if j != n:
                break

            t = i - 1
            temp = hmap.copy()

            while j > 0:
                if s[t] in temp and temp[s[t]] > 0:
                    temp[s[t]] -= 1
                    t -= 1
                    j -= 1
                else:
                    t -= 1

            res = s[t+1:i]
            if len(res) < len(minWin):
                minWin = res
            
            i = t + 2
            j = 0
            temp = hmap.copy()

        return minWin.strip()
