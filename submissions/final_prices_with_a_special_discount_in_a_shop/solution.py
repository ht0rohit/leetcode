class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        st = []
        res = prices.copy()
        
        for i, elem in enumerate(prices):
            while st and st[-1][0] >= elem:
                val, ind = st.pop()
                res[ind] = val - elem

            st.append((elem, i))

        return res