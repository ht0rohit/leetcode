class Solution:
    def minSwaps(self, data: List[int]) -> int:
        n = len(data)
        ones = sum(data)
        
        i, j = 0, 0
        num_ones, max_ones = 0, 0
        
        for j in range(n):
            num_ones += data[j]
            
            if j - i + 1 < ones:
                continue

            max_ones = max(max_ones, num_ones)
            num_ones -= data[i]

            i += 1

        
        return ones - max_ones