class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        n = len(s)
        hmap = {}

        for i in range(n):
            hmap[s[i]] = max(hmap.get(s[i], 0), i)

        res = []
        lastInd = 0
        i, j = 0, 0
        for j in range(n):
            lastInd = max(lastInd, hmap[s[j]])

            if lastInd == j:
                res.append(j - i + 1)
                i = j + 1

        return res            