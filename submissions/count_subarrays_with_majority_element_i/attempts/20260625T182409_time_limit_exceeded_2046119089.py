class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        if target not in nums:
            return 0

        res = 0
        for i in range(1, len(nums) + 1):
            l = 0
            r = l + i
            while r < len(nums) + 1:
                count = 0
                for k in range(l, r):
                    if nums[k] == target:
                        count += 1
                if count > (i // 2):
                    res += 1
                l += 1
                r += 1

        return res