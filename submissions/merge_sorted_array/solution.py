class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        l1, l2 = m + n, n

        i = m
        for j in range(l2):
            nums1[i] = nums2[j]
            
            k = i
            while k > 0 and nums1[k] < nums1[k - 1]:
                nums1[k], nums1[k - 1] = nums1[k - 1], nums1[k]
                k -= 1

            i += 1