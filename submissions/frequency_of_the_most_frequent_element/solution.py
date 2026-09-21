class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        diff = []
        for i in range(len(nums) - 1):
            diff.append(nums[i+1] - nums[i])

        i, j = 0, 0
        maxFreq = 1
        csum = 0
        while j < len(diff):
            freq = j - i + 1
            while csum <= k and j < len(diff):
                temp = diff[j] * (j - i + 1)
                csum += temp
                if csum <= k:
                    freq += 1
                    if freq > maxFreq:
                        maxFreq = freq
                    j += 1
                else:
                    csum -= temp
                    if csum > 0:
                        csum = csum - (nums[j] - nums[i])
                    break

            i += 1
            if i > j:
                j += 1

        return maxFreq