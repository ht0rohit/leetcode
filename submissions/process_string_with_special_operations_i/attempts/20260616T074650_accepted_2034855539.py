class Solution:
    def processStr(self, s: str) -> str:
        result = []

        for elem in s:
            if ord('a') <= ord(elem) <= ord('z'):
                result.append(elem)
            elif elem == '*':
                if result:
                    result.pop()
            elif elem == '#':
                result.extend(result)
            elif elem == '%':
                result.reverse()
            else:
                pass

        return "".join(result)