class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        l = len(s)
        hmap = {}
        revhmap = {}

        for i in range(l):
            if s[i] != t[i] and s[i] in hmap and hmap[s[i]] != t[i]:
                return False

            if t[i] in revhmap and  revhmap[t[i]] != s[i]:
                return False

            hmap[s[i]] = t[i]
            revhmap[t[i]] = s[i]

        return True