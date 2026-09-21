class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res = []
        count = 0

        for elem in s:
            if elem == '(':
                count += 1
                if count > 1:
                    res.append(elem)
            elif elem == ')':
                count -= 1
                if count > 0:
                    res.append(elem)

        return "".join(res)