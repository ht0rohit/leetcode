class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        n, k = len(costs), len(costs[0])
        
        prev_min1 = prev_min2 = float('inf')
        for elem in costs[0]:
            if elem < prev_min1:
                prev_min2 = prev_min1
                prev_min1 = elem

        for i in range(1, n):
            curr_min1 = curr_min2 = float('inf')

            for j in range(k):
                minelem = prev_min1 if costs[i-1][j] != prev_min1 else prev_min2
                costs[i][j] = costs[i][j] + minelem
                
                if costs[i][j] < curr_min1:
                    curr_min2 = curr_min1
                    curr_min1 = costs[i][j]

            prev_min1, prev_min2 = curr_min1, curr_min2
                
        return min(costs[-1])