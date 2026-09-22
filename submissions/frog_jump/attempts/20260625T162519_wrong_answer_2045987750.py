class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if stones[1] != 1:
            return False
        elif len(stones) == 2:
                return True

        jumps = [stones[-1] - stones[i] for i in range(len(stones) - 2, 0, -1)]
        
        def rec(elem, ind):
            if ind == 0:
                return True
            elif ind < 0:
                return False

            k = [elem - 1, elem, elem + 1]
            for e in k:
                if (e > 0) and ((stones[ind] - e) in stones):
                    ind = stones.index(stones[ind] - e)
                    return rec(e, ind)
            else:
                return False

        ind = len(stones) - 1
        for elem in jumps:
            res = rec(elem, ind)
            if res:
                return True
        else:
            return False