class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        n = len(s)
        hmap = {}

        for i in range(n):
            hmap[s[i]] = max(hmap.get(s[i], 0), i)

        res = []
        i = 0
        while i < n:
            length = 0
            lastInd = hmap[s[i]]

            if lastInd == i:
                length = 1
                i += 1
            else:
                temp = lastInd
                for j in range(i + 1, lastInd):
                    nextInd = hmap[s[j]]
                    if nextInd > temp:
                        temp = nextInd

                length = temp - i + 1
                i = temp + 1

            res.append(length)

        return res            