class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hmap = {}
        longS = 0
        i = 0

        for j in range(len(s)):
            hmap[s[j]] = hmap.get(s[j], 0) + 1
            while hmap[s[j]] > 1:
                hmap[s[i]] -= 1
                i += 1
            longS = max(longS, j - i + 1)

        return longS
