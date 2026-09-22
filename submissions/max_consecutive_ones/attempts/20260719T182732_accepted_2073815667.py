class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxc, cont = 0, 0
        for elem in nums:
            if elem == 1:
                cont += 1
            else:
                maxc = max(maxc, cont)
                cont = 0

        return max(maxc, cont)