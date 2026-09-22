class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        def find_max(elem, count):
            nonlocal res

            while st and st[-1][0] > elem:
                if st[-1][0] > 0:
                    count += 1
                res = max([res, st[-1][0], st[-1][0] * (st[-1][1] + count)])
                st.pop()

            if st:
                st[-1][1] += count

            return count


        st = []
        res = 0

        for elem in heights:
            count = find_max(elem, 0)
            st.append([elem, count])

        find_max(-1, 0)

        return res
