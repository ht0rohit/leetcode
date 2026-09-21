class Solution:
    def maxDepth(self, s: str) -> int:
        score = 0
        maxScore = float('-inf')
        for elem in s:
            if elem == '(':
                score += 1
            elif elem == ')':
                score -= 1
            maxScore = max(maxScore, score)

        return maxScore