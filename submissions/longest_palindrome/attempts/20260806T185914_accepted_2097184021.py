class Solution:
    def longestPalindrome(self, s: str) -> int:
        hmap = {}
        for elem in s:
            hmap[elem] = hmap.get(elem, 0) + 1

        res = 0
        flag = 0
        for freq in hmap.values():
            if (freq % 2) == 0:
                res += freq
            else:
                res += freq - 1
                flag = 1

        if flag:
            return res + 1

        return res