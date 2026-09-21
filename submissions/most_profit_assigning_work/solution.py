class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        n = len(difficulty)
        
        hmap = [[d, p] for d, p in zip(difficulty, profit)]
        hmap.sort()
        for i in range(1, n):
            hmap[i][1] = max(hmap[i][1], hmap[i-1][1])

        maxp = 0
        for w in worker:
            l, r = -1, n -1
            
            while l < r:
                mid = (l + r + 1) // 2

                if hmap[mid][0] <= w:
                    l = mid
                else:
                    r = mid - 1
            else:
                maxp = maxp + hmap[l][1] if l >= 0 else maxp + 0

        return maxp