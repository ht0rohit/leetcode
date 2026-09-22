class Solution:
    def validPalindrome(self, s: str) -> bool:
        hmap = Counter(s)

        num_ones = 0
        for v in hmap.values():
            if v == 1:
                num_ones += 1
            if num_ones > 2:
                return False

        return True