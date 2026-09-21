class Solution:
    def maximumValue(self, n: int, s: int, m: int) -> int:
        if n == 1:
            return s
        
        start_up = s + m + ((n - 2) // 2) * (m - 1)
        start_down = s + ((n - 1) // 2) * (m - 1)
        
        return max(start_up, start_down)