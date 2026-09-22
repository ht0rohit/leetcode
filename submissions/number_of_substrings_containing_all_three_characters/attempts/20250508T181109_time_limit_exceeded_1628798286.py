class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        characters = {'a', 'b', 'c'}

        count = 0
        for i in range(0, len(s)-2):
            for j in range(i+2, len(s)):
                if len(characters - set(s[i:j+1])) == 0:
                    count += 1     

        return count