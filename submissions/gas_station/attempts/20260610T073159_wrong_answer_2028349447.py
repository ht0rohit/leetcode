class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        indices = {}
        total = 0
        for i in range(len(gas)):
            indices[i] = gas[i] - cost[i]
            total += indices[i]

        for i in range(len(gas)):
            if indices[i] < 0:
                continue
            elif total >= 0:
                return i
            else:
                return -1