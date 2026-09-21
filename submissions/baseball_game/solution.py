class Solution:
    def calPoints(self, operations: List[str]) -> int:
        l = len(operations)
        scores = []

        for i in range(l):
            if operations[i] == 'C':
                scores.pop()
            elif operations[i] == 'D':
                scores.append(2 * scores[-1])
            elif operations[i] == '+':
                scores.append(scores[-1] + scores[-2])
            else:
                scores.append(int(operations[i]))

        return sum(scores)