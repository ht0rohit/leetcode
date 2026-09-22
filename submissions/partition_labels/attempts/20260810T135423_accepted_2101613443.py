class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        n = len(s)
        hmap = {}

        for i in range(n):
            hmap[s[i]] = max(hmap.get(s[i], 0), i)

        res = []
        q = collections.deque()
        i = 0
        while i < n:
            length = 0
            lastInd = hmap[s[i]]

            if lastInd == i:
                length = 1
                i += 1
            else:
                q.extend(s[i + 1:lastInd])
                temp = lastInd
                
                while q:
                    elem = q.popleft()
                    nextInd = hmap[elem]
                    if nextInd > temp:
                        q.extend(s[temp: nextInd])
                        temp = nextInd

                length = temp - i + 1
                i = temp + 1

            res.append(length)

        return res            