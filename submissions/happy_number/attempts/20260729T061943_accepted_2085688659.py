class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        
        while True:
            sos = 0

            while n:
                elem = n % 10
                n //= 10
                sos += math.pow(elem, 2)
            
            if sos in seen:
                return False
            seen.add(sos)

            if sos == 1:
                return True
            
            n = sos