class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(pos, neg, curr):

            if neg > pos:
                return

            if pos + neg == 2 * n:
                res.append("".join(curr))
                return

            if pos == 0:
                curr.append('(')
                pos += 1
                backtrack(pos, neg, curr)
                curr.pop()
                pos -= 1

            elif pos < n:
                curr.append('(')
                pos += 1
                backtrack(pos, neg, curr)
                curr.pop()
                pos -= 1
                if pos > neg:
                    curr.append(')')
                    neg += 1
                    backtrack(pos, neg, curr)
                    curr.pop()
                    neg -= 1

            elif pos == n and neg < n:
                curr.append(')')
                neg += 1
                backtrack(pos, neg, curr)
                curr.pop()
                neg -= 1

        curr = []
        backtrack(0, 0, curr)

        return res