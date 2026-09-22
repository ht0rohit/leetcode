class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        l = len(row)

        edges = []
        for i in range(1, l, 2):
            edges.append([row[i-1] // 2, row[i] // 2])

        hmap = {}
        for elem in edges:
            if elem[0] != elem[1]:
                if tuple(sorted([elem[0], elem[1]])) in hmap:
                    hmap[tuple(sorted([elem[0], elem[1]]))] += 1
                else:
                    hmap[tuple(sorted([elem[0], elem[1]]))] = 1

        count1, count2, res = 0, 0, 0
        for k, v in hmap.items():
            if v == 1:
                count1 += 1
            elif v == 2:
                count2 += 1
        if count1:
            res += count1 - 1
        if count2:
            res += count2

        return res