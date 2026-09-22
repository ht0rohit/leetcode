class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s = set()
        for elem in nums:
            if elem in s:
                return True
            s.add(elem)
        return False