class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        l = len(s)
        hmap = {'a': 0, 'b': 0, 'c': 0}
        
        i = 0
        count = 0
        for j in range(l):
            hmap[s[j]] += 1

            while hmap['a'] and hmap['b'] and hmap['c']:
                count += l - j
                hmap[s[i]] -= 1
                i += 1

        return count