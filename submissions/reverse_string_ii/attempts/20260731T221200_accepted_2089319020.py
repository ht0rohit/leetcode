class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        n = len(s)
        s = list(s)

        i = tempi = 0
        j = tempj = i + k - 1 if k < n else n - 1
        while j < n:
            while i <= j:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
            
            i = tempi = tempi + 2 * k
            j = tempj = tempj + 2 * k
            if i < n and j >= n:
                j = n - 1

        return "".join(s)