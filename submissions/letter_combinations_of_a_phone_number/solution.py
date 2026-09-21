class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        n = len(digits)
        res = []

        hmap = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'], '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}

        def btrack(i, l, curr):
            if l == n:
                res.append(curr)
                return

            for elem in hmap[digits[i]]:
                btrack(i + 1, l + 1, curr + elem)

        curr = ""
        btrack(0, 0, curr)

        return res