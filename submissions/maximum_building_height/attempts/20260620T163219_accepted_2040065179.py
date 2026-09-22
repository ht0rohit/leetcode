class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        restrictions.append([1, 0])

        found = False
        for r in restrictions:
            if r[0] == n:
                found = True
                break

        if not found:
            restrictions.append([n, n - 1])

        restrictions.sort()

        # left -> right
        for i in range(1, len(restrictions)):
            d = restrictions[i][0] - restrictions[i - 1][0]
            restrictions[i][1] = min(
                restrictions[i][1],
                restrictions[i - 1][1] + d
            )

        # right -> left
        for i in range(len(restrictions) - 2, -1, -1):
            d = restrictions[i + 1][0] - restrictions[i][0]
            restrictions[i][1] = min(
                restrictions[i][1],
                restrictions[i + 1][1] + d
            )

        ans = 0

        for i in range(1, len(restrictions)):
            id1, h1 = restrictions[i - 1]
            id2, h2 = restrictions[i]

            d = id2 - id1
            ans = max(ans, (h1 + h2 + d) // 2)

        return ans