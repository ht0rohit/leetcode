class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        q = collections.deque()
        res = ''
        
        count = 0
        for elem in s:
            if elem == '(':
                count += 1
            elif elem == ')':
                count -= 1
            q.append(elem)
            
            if count == 0:
                q.pop()
                q.popleft()
                res += ''.join(q)
                while q:
                    q.pop()

        return res