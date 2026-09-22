class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
    
        @cache
        def rec(i, cursum):
            
            if i == n:
                return 1 if cursum == target else 0

            count = 0            
            count += rec(i + 1, cursum + nums[i])
            count += rec(i + 1, cursum - nums[i])

            return count


        return rec(0, 0)