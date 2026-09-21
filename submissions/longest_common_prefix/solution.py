class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        l = len(strs)
        prefix = strs[0]
        i = 1

        while i < l:
            a, b = 0, 0
            while a < len(prefix) and b < len(strs[i]):
                if prefix[a] == strs[i][b]:
                    a += 1
                    b += 1
                else:
                    break
            prefix = prefix[:a]
            if not prefix:
                break
            i += 1

        return prefix