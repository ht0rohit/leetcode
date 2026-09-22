class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)

        st = []
        res = False
        for i in range(n):

            while st and st[-1] > nums[i]:
                e = st.pop()
                if st and st[-1] < nums[i]:
                    res = True
                    break

            st.append(nums[i])


        return res