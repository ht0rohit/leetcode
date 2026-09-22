class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        l = len(nums2)
        hset = {elem: i for i, elem in enumerate(nums2)}
        nums2_res = [-1] * l
        nums1_res = []
        st = []

        for i in range(l):
            if not st:
                st.append(nums2[i])
                continue

            while st and st[-1] < nums2[i]:
                nums2_res[hset[st[-1]]] = nums2[i]
                st.pop()
            st.append(nums2[i])

        for elem in nums1:
            nums1_res.append(nums2_res[hset[elem]])

        return nums1_res