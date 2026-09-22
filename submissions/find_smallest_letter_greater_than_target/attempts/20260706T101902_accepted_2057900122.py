class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l = len(letters)
        i, j = 0, l - 1

        while i <= j:
            mid = i + (j - i) // 2
            if letters[mid] <= target:
                i = mid + 1
            else:
                j = mid - 1

        return letters[i % l]

                