class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        l = len(s)
        jump = [True] + [False] * (l - 1)
        
        for i in range(len(s)):
            if jump[i]:
                for j in range(i + minJump, i + maxJump + 1):
                    if j < l and s[j] == '0':
                        jump[j] = True

        return jump[-1]