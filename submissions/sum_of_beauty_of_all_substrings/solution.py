class Solution:
    def beautySum(self, s: str) -> int:
        n = len(s)

        res = 0
        for i in range(n):
            freq = [0] * 26
            maxFreq = 0
            for j in range(i, n):
                ind = ord(s[j]) - ord('a')
                freq[ind] += 1
                maxFreq = max(maxFreq, freq[ind])
                res += maxFreq - min(x for x in freq if x)

        return res