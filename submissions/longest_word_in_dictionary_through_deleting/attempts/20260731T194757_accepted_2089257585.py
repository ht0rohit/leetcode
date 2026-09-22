class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        m = len(s)
        dictionary.sort(key=len, reverse=True)

        res = ""
        for elem in dictionary:
            n = len(elem)
            if n <= m:
                i, j = 0, 0

                while i < m and j < n:
                    if s[i] == elem[j]:
                        j += 1
                    i += 1

                if j == n:
                    if len(elem) > len(res):
                        res = elem
                    elif len(elem) == len(res) and res > elem:
                        res = elem

        return res
