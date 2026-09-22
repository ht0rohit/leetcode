class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if n == 1:
            return [nums[0]]

        q = deque()
        res = []

        for i in range(k):
            while q and nums[q[-1]] <= nums[i]:
                q.pop()
            q.append(i)

        res.append(nums[q[0]])

        for i in range(k, n):
            while q and nums[q[-1]] <= nums[i]:
                q.pop()
            q.append(i)

            if q and q[0] < i - k + 1:
                q.popleft()

            res.append(nums[q[0]])
            
        return res