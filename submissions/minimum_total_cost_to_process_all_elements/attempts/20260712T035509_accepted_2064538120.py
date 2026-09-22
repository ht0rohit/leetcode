class Solution:
    def minimumCost(self, nums: list[int], k: int) -> int:
        # Looks easy O(n)
        MOD = 10**9 + 7
        l = len(nums)

        cost = 1
        tempk = k
        res = 0

        i = 0
        while i < l:
            if nums[i] <= tempk:
                tempk -= nums[i]
                i += 1
            else:
                req = (nums[i] - tempk + k - 1) // k
                res = (res + req * (2 * cost + req - 1) // 2) % MOD
                tempk += req * k
                cost += req
                    
        return res