class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        maj = None
        for elem in nums:
            if not count:
                maj = elem
            count += 1 if elem == maj else -1

        return maj