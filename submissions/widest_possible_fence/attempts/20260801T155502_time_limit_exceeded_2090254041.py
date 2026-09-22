class Solution:
    def maximumWidth(self, planks: list[int]) -> int:
        hmap = Counter(planks)
        ptype = sorted(hmap)

        res = 0
        for p in range(ptype[0], ptype[-1] * 2 + 1):
            width = hmap.get(p, 0)

            for a in ptype:
                b = p - a

                if a > b:
                    break

                if b not in hmap:
                    continue

                if a == b:
                    width += hmap[a] // 2
                else:
                    width += min(hmap[a], hmap[b])

            res = max(res, width)

        return res
