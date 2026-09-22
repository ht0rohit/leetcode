class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1:
            return n

        l = len(trust)
        if l != n - 1:
            return -1

        judge = trust[0][1]
        i = 0
        while i < l:
            if trust[i][1] != judge:
                return -1
            i += 1
        else:
            return judge
