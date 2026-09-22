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
                else:
                    return False
            elif ind < 1:
                return False
        
            k = [elem - 1, elem, elem + 1]
            for e in k:
                if (e > 0) and ((stones[ind] - e) in stones):
                    ind = stones.index(stones[ind] - e)
                    return rec(e, ind)
            else:
                return False
        
        ind = l - 1
        for i in range(len(jumps)): 
            res = rec(jumps[i], ind)
            if res:
                return True
        else:
            return False