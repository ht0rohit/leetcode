class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        n = len(nums)
        res = 0

        if k == 0:
            hmap = Counter(nums)
            for elem in hmap:
                if hmap[elem] > 1:
                    res += 1
            
            return res

        hset = set()
        for i in range(n):
            if nums[i] not in hset:
                if nums[i] - k in hset:
                    res += 1
                if nums[i] + k in hset:
                    res += 1
                
            hset.add(nums[i])


        return res