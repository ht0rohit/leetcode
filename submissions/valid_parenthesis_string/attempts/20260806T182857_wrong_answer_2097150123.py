class Solution:
    def checkValidString(self, s: str) -> bool:
        n = len(s)
        score = 0
        star = 0

        for elem in s:
            if elem == '(':
                score += 1
            elif elem == ')':
                score -= 1
            else:
                star += 1

        l = abs(star - score) // 2
        r = star - l

        if score == 0:
            return True
        if score > 0 and score + l - r == 0:
            return True
        if score < 0 and score + l - r == 0:
            return True
        return False