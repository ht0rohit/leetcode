class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        l = len(cost)
        if l == 2:
            return min(cost[0], cost[1])

        cost.append(0)
        step1, step2 = cost[0], cost[1]
        for i in range(2, l + 1):
            step = min(step1, step2) + cost[i]
            step1 = step2
            step2 = step

        return step