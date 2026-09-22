class Solution:
    def maxProduct(self, n: int) -> int:
        first_max, second_max = 0, 0
        while n:
            elem = n % 10
            if elem > first_max:
                second_max = first_max
                first_max = elem
            elif elem > second_max and elem <= first_max:
                second_max = elem 
            n //= 10

        return first_max * second_max