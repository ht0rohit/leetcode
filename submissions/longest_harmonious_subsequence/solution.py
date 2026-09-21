class Solution:
    def findLHS(self, nums: List[int]) -> int:
        hmap = Counter(nums)

        maxlen = 0
        for elem in nums:
            found = hmap.get(elem + 1, 0)
            if found:
                maxlen = max(maxlen, hmap[elem] + found)


        return maxlen