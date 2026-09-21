class Solution:
    def canCross(self, stones: List[int]) -> bool:
        n = len(stones)
        stones_set = {elem: i for i, elem in enumerate(stones)}
        
        @cache
        def rec(i, jump):
            if i == n - 1:
                return True
            
            jumps = [jump - 1, jump, jump + 1]
            for k in jumps:
                if k > 0:
                    if stones[i] + k in stones_set:
                        if rec(stones_set[stones[i] + k], k):
                            return True

            return False

        return rec(0, 0)