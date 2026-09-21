class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        nums.sort()

        psum = [0] * n
        psum[0] = nums[0]
        for i in range(1, n):
            psum[i] = psum[i - 1] + nums[i]
        
        res = []
        for elem in queries:
            l, r = 0, n

            while l < r:
                mid = l + (r - l) // 2
                if nums[mid] >= elem:
                    r = mid
                else:
                    l = mid + 1

            leftsum = elem * l - psum[l - 1] if l > 0 else 0
            rightsum = psum[n - 1] - psum[l - 1] - elem * (n - l) if l > 0 else psum[n - 1] - elem * n
            
            res.append(leftsum + rightsum)

        return res 