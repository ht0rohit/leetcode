class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = len(nums)
        if l == 1:
            return [nums[0]]

        d = deque()
        res = []
        for i in range(k):
            if not d or d[-1][0] > nums[i]:
                d.append((nums[i], i))
            else:
                while d and d[-1][0] <= nums[i]:
                    d.pop()
                d.append((nums[i], i))

        res.append(d[0][0])

        for i in range(k, l):
            if d[0][1] < (i - k + 1):
                d.popleft()
            if not d or d[-1][0] > nums[i]:
                d.append((nums[i], i))
            else:
                while d and d[-1][0] <= nums[i]:
                    d.pop()
                d.append((nums[i], i))
            res.append(d[0][0])

        return res