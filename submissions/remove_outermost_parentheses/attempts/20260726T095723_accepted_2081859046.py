class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        q = []
        count = 0

        for elem in s:
            if count == 0:
                q.append([])
            if elem == '(':
                count += 1
            elif elem == ')':
                count -= 1
            q[-1].append(elem)

        res = []
        for elem in q:
            res.extend(elem[1:-1])
        res = "".join(res)

        return res