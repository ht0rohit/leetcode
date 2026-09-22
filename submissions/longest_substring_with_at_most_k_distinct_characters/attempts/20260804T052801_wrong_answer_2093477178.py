class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        n = len(s)
        hset = set()
        distinct = 0
        res = 0

        i, j = 0, 0
        while j < n:
            if s[j] not in hset:
                hset.add(s[j])
                distinct += 1
            
            if distinct <= k:
                res = max(res, j - i + 1)
                j += 1
            
            if distinct > k:
                while distinct > k:
                    if s[i] in hset:
                        hset.discard(s[i])
                        distinct -= 1
                        i += 1
                j += 1

        return res
