class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hset = set(nums)
        visited = set()

        res, cons = 0, 0
        for elem in nums:
            if elem not in visited:
                visited.add(elem)
                cons = 1
                
                while elem + 1 in hset:
                    visited.add(elem + 1)
                    cons += 1
                    elem += 1
                
                res = max(res, cons)

            
        return res