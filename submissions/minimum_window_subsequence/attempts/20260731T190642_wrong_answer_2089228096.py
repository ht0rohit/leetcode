class Solution:
    def minWindow(self, s1: str, s2: str) -> str:
        m, n = len(s1), len(s2)
        if n > m:
            return ""
        
        minWin = ""
        firstIndex = None

        i, j = 0, 0
        while i < m:

            # Forward pass
            while i < m and j < n:
                if s1[i] == s2[j]:
                    if j == 0:
                        firstIndex = i
                    j += 1
                i += 1

            if i == m and j != n:
                break

            # Backward pass
            temp, j = i - 1, n - 1
            while temp > firstIndex - 1 and j >= 0:
                if s1[temp] == s2[j]:
                    j -= 1
                temp -= 1
            j = 0

            win = s1[temp+1:i]
            if not minWin or len(minWin) > len(win): 
                minWin = win

        return minWin
