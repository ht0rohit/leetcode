class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False

        q = collections.deque([nums[0], nums[1]])
        
        for i in range(2, n):
            if q[1] > nums[i] and nums[i] > q[0]:
                return True

            q.popleft()
            q.append(nums[i])

        return False