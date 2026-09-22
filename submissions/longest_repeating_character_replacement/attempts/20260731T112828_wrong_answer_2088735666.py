class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        hmap = Counter(s)
        maxF = max(hmap, key = hmap.get)

        i, j = 0, 0
        longS, currS = 0, 0

        for j in range(n):
            currS += 1
            if s[j] != maxF and k > 0:
                k -= 1
            elif s[j] != maxF and k == 0:
                while s[i] == maxF:
                    i += 1
                i += 1
                k += 1
                currS = j - i + 1
            
            longS = max(longS, currS)

        return longS