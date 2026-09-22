class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        st = []
        
        for elem in num:
            while st and st[-1] > elem and k:
                st.pop()
                k -= 1
            st.append(elem)

        if k:
            st = st[:-k]
        res = "".join(st).lstrip('0')


        return res if res else '0'