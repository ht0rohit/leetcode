class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l = len(nums)
        if k == 0 or l == 1:
            return False

        hmap = {}

        for i in range(l):
            if nums[i] in hmap:
                if abs(hmap[nums[i]] - i) <= k:
                    return True
            hmap[nums[i]] = i
        
        return False