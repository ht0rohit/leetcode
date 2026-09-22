class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        l = len(arr)
        i, j = 0, l - 1
        missing = 0

        while i <= j:
            mid = i + (j - i) // 2
            missing = arr[mid] - (mid + 1)
            if missing < k:
                i = mid + 1
            else:
                j = mid - 1

        return i + k