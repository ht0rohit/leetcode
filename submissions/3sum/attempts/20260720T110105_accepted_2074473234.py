class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = set()
        
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            hset = set()
            target = 0 - nums[i]
            
            for j in range(i+1, len(nums)):
                if target - nums[j] in hset:
                    triplet = tuple(sorted([nums[i], nums[j], target - nums[j]]))
                    res.add(triplet)
                
                hset.add(nums[j])

        return list(res)