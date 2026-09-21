class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        m, n = len(s), len(p)

        hmap = Counter(p)
        distinct = len(hmap)
        anagram = {}
        found = 0

        res = []
        i, j = 0, 0
        while j < m:
            anagram[s[j]]  = anagram.get(s[j], 0) + 1
            if s[j] in hmap and anagram[s[j]] == hmap[s[j]]:
                found += 1

            if j - i + 1 < n:
                j += 1
                continue

            if found == distinct:
                res.append(i)
            
            if s[i] in hmap and anagram[s[i]] == hmap[s[i]]:
                found -= 1
            anagram[s[i]] -= 1

            i += 1
            j += 1

        return res
