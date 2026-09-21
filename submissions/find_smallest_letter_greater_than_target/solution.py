class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l = len(letters)
        
        i, j = 0, l
        while i < j:
            mid = (i + j) // 2
            if letters[mid] > target:
                j = mid
            else:
                i = mid + 1
        
        return letters[i % l]
