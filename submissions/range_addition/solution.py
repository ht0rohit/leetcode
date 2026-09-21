class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        n = length
        diff = [0] * n

        for l, r, seats in updates:
            diff[l] += seats
            if r + 1 < n:
                diff[r+1] -= seats

        for i in range(1, n):
            diff[i] += diff[i - 1]

        return diff