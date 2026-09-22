class Solution:
    def canMakeSubsequence(self, s: str, t: str) -> bool:
        no_change = 0
        one_change = -1

        for ch in t:
            prev0, prev1 = no_change, one_change

            if prev0 < len(s) and s[prev0] == ch:
                no_change += 1

            if prev1 != -1 and prev1 < len(s) and s[prev1] == ch:
                one_change = max(one_change, prev1 + 1)

            if prev0 < len(s):
                one_change = max(one_change, prev0 + 1)

        res = no_change == len(s) or one_change == len(s)
        return res