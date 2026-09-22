class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n = len(nums)

        i, j = 0, 0
        zcount = 0
        maxlen = 0

        for j in range(n):
            if nums[j] == 0:
                zcount += 1

            while zcount > 1:
                if nums[i] == 0:
                    zcount -= 1
                i += 1

            maxlen = max(maxlen, j - i + 1)

        return maxlen