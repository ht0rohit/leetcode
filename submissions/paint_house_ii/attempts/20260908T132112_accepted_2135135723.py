class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        n, k = len(costs), len(costs[0])
    
        for i in range(1, n):
            for j in range(k):
                costs[i][j] = costs[i][j] + min(costs[i-1][0:j] + costs[i-1][j+1:])
                
        return min(costs[-1])