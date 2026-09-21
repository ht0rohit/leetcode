class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums1)
        
        hmap = {nums1[i]: i for i in range(n)}
        
        st = []
        res = [-1] * n
        for elem in nums2:
            while st and st[-1] < elem:
                p = st.pop()
                if p in hmap:
                    res[hmap[p]] = elem

            st.append(elem)

        return res