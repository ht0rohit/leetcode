class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        maj = None
        for elem in nums:
            if not maj or not count:
                maj = elem
            count += 1 if nums == maj else -1

        return maj