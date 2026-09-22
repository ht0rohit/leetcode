class Solution:
    def minimumPushes(self, word: str) -> int:
        hmap = {}
        for elem in word:
            if elem in hmap:
                hmap[elem] += 1
            else:
                hmap[elem] = 1
        hmap = dict(sorted(hmap.items(), key=lambda x: x[1], reverse = True))

        res = 0
        for i, (k, v) in enumerate(hmap.items()):
            mul = i // 8
            res += v * (mul + 1)

        return res