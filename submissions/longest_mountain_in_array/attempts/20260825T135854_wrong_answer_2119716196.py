class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        n = len(arr)
        if n < 3:
            return 0
        
        res = 0
        numl, numr = 0, 0
        for i in range(1, n):
            
            if arr[i] < arr[i-1]:
                if numl:
                    numr += 1

            elif arr[i] > arr[i-1]:
                if not numr:
                    numl += 1
                else:
                    res = max(res, numl + numr + 1)
                    numl, numr = 0, 0
            
            else:
                if numl and numr:
                    res = max(res, numl + numr + 1)
                numl, numr = 0, 0

            if numl and numr:
                res = max(res, numl + numr + 1)
                
        
        return res