class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        l = len(colors)
        res = 0
        for i in range(l):
            if colors[i] == colors[(i+2) % l] and colors[i] != colors[(i+1) % l]:
                res += 1

        return res