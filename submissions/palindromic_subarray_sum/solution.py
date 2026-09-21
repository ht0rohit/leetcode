class Solution:
    def getSum(self, nums: List[int]) -> int:
        # [7,1,2,1,7,7,1,2,1,7]
        # [1,1,1,2,1,1,1,1]
        
        n = len(nums)

        # Prefix sum
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        def find_radius(is_even):
            radius_arr = [0] * n
            win_left = 0
            win_right = -1

            for i in range(n):
                if i > win_right:
                    radius = 0 if is_even else 1
                else:
                    if is_even:
                        mirror = win_left + win_right - i + 1
                    else:
                        mirror = win_left + win_right - i

                    radius = min(radius_arr[mirror], win_right - i + 1)

                while True:
                    if is_even:
                        left = i - radius - 1
                        right = i + radius
                    else:
                        left = i - radius
                        right = i + radius

                    if (
                        left < 0
                        or right >= n
                        or nums[left] != nums[right]
                    ):
                        break

                    radius += 1

                radius_arr[i] = radius

                if is_even:
                    new_left = i - radius
                    new_right = i + radius - 1
                else:
                    new_left = i - radius + 1
                    new_right = i + radius - 1

                if new_right > win_right:
                    win_left = new_left
                    win_right = new_right

            return radius_arr

        odd_rad = find_radius(False)
        even_rad = find_radius(True)

        ans = max(nums)

        for i in range(n):
            # Odd palindrome
            left = i - odd_rad[i] + 1
            right = i + odd_rad[i] - 1
            ans = max(ans, prefix[right + 1] - prefix[left])

            # Even palindrome
            if even_rad[i]:
                left = i - even_rad[i]
                right = i + even_rad[i] - 1
                ans = max(ans, prefix[right + 1] - prefix[left])

        return ans
