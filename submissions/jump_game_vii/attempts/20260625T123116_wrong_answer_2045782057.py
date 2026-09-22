class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        l = len(s)
        reach = [True] + [False] * (l - 1)

        for jump in range(minJump, min(maxJump + 1, l)):
            if s[jump] == '0':
                reach[jump] = True
        jump = minJump + 1

        for i in range(1, len(s) - minJump):
            if reach[i]:
                if s[jump] == '0':
                    reach[jump] = True
            jump += 1

        return reach[-1]