class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        st = []

        res = 0
        for i in range(n):

            if st and height[i] >= st[0]:
                minHeight = min(st[0], height[i])
                
                while st and st[-1] <= height[i]:
                    e = st.pop()
                    res += minHeight - e

            st.append(height[i])

        minHeight = 0
        while len(st) > 1:
            minHeight = max(minHeight, min(st[0], st[-1]))
            e = st.pop()
            res += max(0, minHeight - st[-1])


        return res