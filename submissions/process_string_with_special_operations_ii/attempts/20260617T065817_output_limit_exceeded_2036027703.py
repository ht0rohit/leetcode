class Solution:
    def processStr(self, s: str, k: int) -> str:
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

        result = "".join(result)
        print(result)
        if k < len(result):
            return result[k]
        else:
            return '.'