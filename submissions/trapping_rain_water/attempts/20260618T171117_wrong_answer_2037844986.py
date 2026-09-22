class Solution:
    def trap(self, height: List[int]) -> int:
        trap = [0] * len(height)
        
        max = 0
        maxWater = 0
        i, j = 0, 0

        while j < len(height):
            if height[j] >= max:
                max = height[j]
                maxWater += sum(trap[i+1:j])
                i = j
            elif height[j] < max and j != len(height) - 1:
                trap[j] = max - height[j]
            else:
                if height[j] > height[j-1]:
                    diff = max - height[j]
                    maxWater += sum(trap[i+1 : j]) - sum([diff if trap[k] >= diff else trap[k] for k in range(i+1, j)])
                elif height[j] < height[j-1]:
                    diff = max - height[j-1]
                    maxWater += sum(trap[i+1 : j-1]) - sum([diff if trap[k] >= diff else trap[k] for k in range(i+1, j-1)])

            j += 1

        return maxWater