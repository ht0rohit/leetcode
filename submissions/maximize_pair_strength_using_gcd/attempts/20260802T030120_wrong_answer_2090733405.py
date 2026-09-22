class Solution:
    def maxPairStrength(self, nums: list[int]) -> int:
        n = len(nums)
        
        res = 0
        for i in range(n):
            for j in range(i + 1, n):
                g = gcd(nums[i], nums[j])
                ans = max(res, (nums[i] // g) * (nums[j] // g))

        return res

    # gcd(a,b) = g
    # a = gx or x = a/g
    # b = gy or y = b/g
    # strength = ab / gcd(a,b) = g^2xy/g^2 = a/g * b/g
