class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        if sum(gas) < sum(cost):
            return -1

        currGas = 0
        startInd = 0
        for i in range(n):
            currGas += gas[i] 
            
            if currGas < cost[i]:
                currGas = 0
                startInd = i + 1

        return startInd
        