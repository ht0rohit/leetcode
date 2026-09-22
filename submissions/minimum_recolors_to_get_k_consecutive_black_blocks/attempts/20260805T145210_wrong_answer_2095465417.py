class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)
        
        numb = 0
        for i in range(k):
            if blocks[i] == 'B':
                numb += 1
        minv = k - numb

        for j in range(k, n - 1):
            if blocks[j - k] == 'W' and blocks[j] == 'B':
                numb += 1
            elif blocks[j - k] == 'B' and blocks[j] == 'W':
                numb -= 1

            diff = k - numb
            minv = min(minv, diff)

        return minv
