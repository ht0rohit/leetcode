class Solution:
    def processStr(self, s: str) -> str:
        result = ""
        for elem in s:
            if ord('a') <= ord(elem) <= ord('z'):
                result += elem
            elif elem == '*':
                result = result[:-1]
            elif elem == '#':
                result += result
            elif elem == '%':
                result = result[::-1]
            else:
                pass
                
        return result