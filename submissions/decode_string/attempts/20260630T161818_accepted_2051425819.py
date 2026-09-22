class Solution:
    def decodeString(self, s: str) -> str:
        l = len(s)
        st = []

        temp_s, temp_i = '', ''
        res = ''
        for i in range(l):
            if s[i].isalnum() or s[i] == '[':
                st.append(s[i])
            elif s[i] == ']':
                while st and st[-1].isalpha():
                    temp_s = st[-1] + temp_s
                    st.pop()
                st.pop()
                while st and st[-1].isdigit():
                    temp_i = st[-1] + temp_i
                    st.pop()
                if st:
                    temp_s = int(temp_i) * temp_s
                    st.append(temp_s)
                else:
                    res += int(temp_i) * temp_s
                temp_s, temp_i = '', ''
        else:
            while st:
                temp_s = st[-1] + temp_s
                st.pop()
            res += temp_s

        return res
