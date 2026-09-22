class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)

        st = []

        res = 0
        for elem in heights:
            
            count = 0
            while st and st[-1] > elem:
                count += 1
                res = max([res, st[-1], st[-1] * count])
                st.pop()
            st.append(elem)

        count = 0
        while st:
            count += 1
            res = max([res, st[-1], st[-1] * count])
            st.pop()

        return res
