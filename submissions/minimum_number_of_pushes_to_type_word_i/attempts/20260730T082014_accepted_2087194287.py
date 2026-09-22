class Solution:
    def minimumPushes(self, word: str) -> int:
        n = len(word)
        keys = 8
        rep = n // keys
        rem = n % keys
        
        return rem if n < keys else (8 * ((rep * (rep + 1)) // 2)) + ((rep + 1) * rem)