class Solution:
    def canCross(self, stones: List[int]) -> bool:
        l = len(stones)
        if stones[1] != 1:
            return False
        elif l == 2:
            return True

        jumps = [stones[-1] - stones[i] for i in range(l - 2, 0, -1)]
        
        def rec(elem, ind):
            if ind == 1:
                if elem in [0, 1, 2]:
                    return True
                return False
            elif ind < 1:
                return False

            k = [elem - 1, elem, elem + 1]
            indl = [-1] * len(k)        
            for i, e in enumerate(k):
                if (e > 0) and (stones[ind] - e) in stones:
                    indl[i] = stones.index(stones[ind] - e)
            return rec(k[0], indl[0]) or rec(k[1], indl[1]) or rec(k[2], indl[2])
        
        ind = l - 1
        for elem in jumps:
            ind -= 1
            res = rec(elem, ind)
            if res:
                return True
        else:
            return False