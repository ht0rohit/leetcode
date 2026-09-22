class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        n = len(prices)
        
        st = []
        res = 0
        for elem in prices:
            
            if st and (st[-1] <= elem or st[-1] - elem > 1):
                while st:
                    st.pop()

            st.append(elem)
            res += len(st)

        return res
