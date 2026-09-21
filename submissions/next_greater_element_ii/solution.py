class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        st = []

        res = [-1] * n
        for i in range(2 * n):

            while st and nums[st[-1]] < nums[i%n]:
                elem = st.pop()
                res[elem] = nums[i%n]

            st.append(i%n)


        return res