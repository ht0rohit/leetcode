class Solution:
    def isValid(self, s: str) -> bool:
        hmap = {')': '(', ']': '[', '}': '{'}
        stack = []

        for elem in s:
            if stack:
                if stack[-1] == hmap.get(elem, ''):
                    stack.pop()
                    continue
                else:
                    stack.append(elem)
            else:
                stack.append(elem)

        if stack:
            return False
        return True