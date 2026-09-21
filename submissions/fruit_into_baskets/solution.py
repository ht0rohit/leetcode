class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n = len(fruits)
        hmap = {}
        
        res = 0
        i = 0
        for j in range(n):
            hmap[fruits[j]] = hmap.get(fruits[j], 0) + 1
            
            while len(hmap) > 2:
                hmap[fruits[i]] -= 1
                if hmap[fruits[i]] == 0:
                    del hmap[fruits[i]]
                i += 1

            res = max(res, j - i + 1)

        return res
