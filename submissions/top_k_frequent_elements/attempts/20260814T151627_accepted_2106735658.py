class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)

        hmap = Counter(nums)
        bucket = [[] for _ in range(n+1)]

        for key, value in hmap.items():
            bucket[value].append(key)

        bucket = [e for elem in bucket for e in elem]

        return bucket[-k:]