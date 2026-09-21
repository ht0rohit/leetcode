class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        answer = []
        answer += [list(set(nums1) - set(nums2))]
        answer += [list(set(nums2) - set(nums1))]
        return answer