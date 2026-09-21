class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height) - 1

        maxVol = 0
        while i < j:
            vol = min(height[i], height[j]) * (j - i)
            if vol > maxVol:
                maxVol = vol
            if height[i] <= height[j]:
                i += 1
            else:
                j -= 1

        return maxVol