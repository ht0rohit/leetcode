class Solution:
    def minimumPushes(self, word: str) -> int:
        n = len(word)
        return n + (n % 8)