class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        n = len(s)
        hmap = {}
        res = 0

        i, j = 0, 0
        while j < n:
            hmap[s[j]] = hmap.get(s[j], 0) + 1
            
            while len(hmap) > k:
                hmap[s[i]] -= 1
                if hmap[s[i]] == 0:
                    del hmap[s[i]]
                i += 1

            res = max(res, j - i + 1)

            j += 1

        return res
