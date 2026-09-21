class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        op = ['+', '-', '*', '/']
        
        for elem in tokens:
            if elem not in op:
                stack.append(int(elem))
            else:
                a = stack.pop()
                b = stack.pop()
                if elem == '+':
                    res = b + a
                elif elem == '-':
                    res = b - a
                elif elem == '*':
                    res = b * a
                elif elem == '/':
                    res = int(b / a)
                stack.append(res)

        return stack[0]