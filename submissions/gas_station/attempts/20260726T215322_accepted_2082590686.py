class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        if sum(gas) < sum(cost):
            return -1

        i = 0
        currGas = 0
        while i < n:
            if currGas + gas[i] < cost[i]:
                i += 1
                currGas = 0
                continue
            else:
                j = i
                while currGas + gas[j % n] >= cost[j % n]:
                    currGas += gas[j % n] - cost[j % n]
                    j += 1
                    if j % n == i:
                        return j % n
                if j < n:
                    i = j
                else:
                    return - 1
                currGas = 0
        else:
            return -1