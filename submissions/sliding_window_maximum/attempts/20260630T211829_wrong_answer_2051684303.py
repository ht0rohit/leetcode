class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = len(nums)
        if l == 1:
            return [nums[0]]

        d = deque()
        d.append(0)
        res = []

        for i in range(1, l):
            if d[0] < (i - k + 1):
                d.popleft()
            if not d or nums[d[-1]] > nums[i]:
                d.append(i)
            else:
                while d and nums[d[-1]] <= nums[i]:
                    d.pop()
                d.append(i)
            if i + 1 >= k:
                res.append(nums[d[0]])

        return res