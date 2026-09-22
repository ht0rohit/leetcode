class Solution:
    def simplifyPath(self, path: str) -> str:
        path = re.sub(r"/+", "/", path)
        path = path.split('/')
        l = len(path)
        st = ['/']

        for i in range(1, l):
            if len(st) == 1:
                if path[i] != '.' and path[i] != '..':
                    st.append(path[i])
            elif path[i] == '.':
                pass
            elif path[i] == '..':
                st.pop()
                st.pop()
            elif path[i] != '':
                st.append('/')
                st.append(path[i])

        return "".join(st)