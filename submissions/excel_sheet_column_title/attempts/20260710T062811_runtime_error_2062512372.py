class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        a = ord('A') - 1
        mul = columnNumber // 26
        rem = columnNumber % 26
        
        res = ''
        if mul > 0:
            res += chr(a + mul)
        res += chr(a + rem)

        return res