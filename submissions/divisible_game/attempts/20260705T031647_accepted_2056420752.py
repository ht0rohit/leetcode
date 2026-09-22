class Solution:
    def divisibleGame(self, nums: list[int]) -> int:
        MOD = math.pow(10, 9) + 7

        divisors = {2}
        max_num = max(nums)

        for num in nums:
            divisor = 2
            while divisor * divisor <= num:
                if num % divisor == 0:
                    divisors.add(divisor)
                    divisors.add(num // divisor)
                divisor += 1

            if num > 1:
                divisors.add(num)

        best_diff = -max_num * len(nums) - 1
        best_k = 2

        for k in divisors:
            current_sum = 0
            max_sum = -max_num * len(nums) - 1

            for num in nums:
                if num % k == 0:
                    value = num
                else:
                    value = -num

                current_sum = max(value, current_sum + value)
                max_sum = max(max_sum, current_sum)

            if max_sum > best_diff or (max_sum == best_diff and k < best_k):
                best_diff = max_sum
                best_k = k

        res = (best_diff * best_k) % MOD
        return int(res)