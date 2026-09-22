class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        n = len(s)
        st = []

        for elem in s:
            if st and st[-1] == '(' and elem == ')':
                st.pop()
            else:
                st.append(elem)

        return len(st)    