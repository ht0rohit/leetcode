class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        count = 0
        for elem in patterns:
            if elem in word:
                count += 1

        return count