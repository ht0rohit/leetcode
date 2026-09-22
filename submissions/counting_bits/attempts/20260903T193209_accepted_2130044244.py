class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0] * (n + 1)
        for i in range(1, n + 1):
            m = i
            
            while m:
                m &= (m - 1)
                res[i] += 1
                
                
        return res