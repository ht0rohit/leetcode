class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        lis = list(num)
        n = len(lis)
        
        i = 0
        for j in range(1, n):
            if not k:
                break
                
            if lis[i] > lis[j]:
                lis[i] = ''        
                i = j
                k -= 1
            else:
                i += 1
        
        res = ''.join(lis)
        if k:
            res = res[:-k]
        res = res.lstrip('0')
        
        return res if res else '0'