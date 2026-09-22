class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hset = set(nums)

        res = 0
        for elem in hset:
            if elem - 1 not in hset:
                curr = elem
                cons = 1
                
                while curr + 1 in hset:
                    cons += 1
                    curr += 1
                
                res = max(res, cons)

            
        return res