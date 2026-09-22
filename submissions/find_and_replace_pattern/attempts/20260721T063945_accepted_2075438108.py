class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        l = len(pattern)
        res = []

        for elem in words:
            hmap = {}
            revhmap = {}

            for i in range(l):
                if elem[i] in hmap and hmap[elem[i]] != pattern[i]:
                    break

                if pattern[i] in revhmap and  revhmap[pattern[i]] != elem[i]:
                    break

                hmap[elem[i]] = pattern[i]
                revhmap[pattern[i]] = elem[i]

            else:
                res.append(elem)

        return res