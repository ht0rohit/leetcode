class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        n = len(arr)
        if n < 3:
            return 0
        
        res = 0
        numl, numr = 0, 0
        for i in range(1, n):
            
            if arr[i] < arr[i-1] and numl:
                numr += 1

            elif arr[i] > arr[i-1]:
                if numr:
                    numl, numr = 1, 0
                else:
                    numl += 1

            else:
                numl, numr = 0, 0

            if numl and numr:
                res = max(res, numl + numr + 1)

 
        return res