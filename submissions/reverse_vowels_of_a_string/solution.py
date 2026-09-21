class Solution:
    def reverseVowels(self, s: str) -> str:
        n = len(s)
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

        i, j = 0, n-1
        res = [''] * n

        while i <= j:
            
            while i <= j and s[i] not in vowels:
                res[i] = s[i]
                i += 1

            while i <= j and s[j] not in vowels:
                res[j] = s[j]
                j -= 1

            if i <= j:
                res[i] = s[j]
                res[j] = s[i]
                i += 1
                j -= 1

        return "".join(res)
