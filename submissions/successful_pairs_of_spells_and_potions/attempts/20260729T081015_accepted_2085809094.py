class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        n, m = len(spells), len(potions)
        potions.sort()

        res = []
        for elem in spells:
            target = math.ceil(success / elem)
            l, r = 0, m
            
            while l < r:
                mid = l + (r - l) // 2

                if potions[mid] >= target:
                    r = mid
                else:
                    l = mid + 1

            res.append(m - l)

        return res