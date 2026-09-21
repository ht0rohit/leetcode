class Solution:
    def maxDigitRange(self, nums: list[int]) -> int:
        
        def get_digit_range(number):
            number = abs(number)

            smallest_digit = 9
            largest_digit = 0

            while number:
                digit = number % 10
                smallest_digit = min(smallest_digit, digit)
                largest_digit = max(largest_digit, digit)
                number //= 10

            return largest_digit - smallest_digit

        maximum_digit_range = 0
        digit_ranges = []

        for number in nums:
            current_range = get_digit_range(number)
            digit_ranges.append(current_range)
            maximum_digit_range = max(maximum_digit_range, current_range)

        total_sum = 0

        for number, digit_range in zip(nums, digit_ranges):
            if digit_range == maximum_digit_range:
                total_sum += number

        return total_sum
            