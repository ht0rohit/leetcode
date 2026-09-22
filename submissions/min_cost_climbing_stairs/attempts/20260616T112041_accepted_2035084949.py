class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) == 2:
            return min(cost[0], cost[1])
        
        min_cost = [0, 0] + [-1] * (len(cost) - 1)

        for i in range(2, len(cost) + 1):
            min_cost[i] = min(min_cost[i-1] + cost[i-1], min_cost[i-2] + cost[i-2])

        return min_cost[-1]