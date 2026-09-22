class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)

        hmap = Counter(nums)
        bucket = [[] for _ in range(n+1)]

        for k, v in hmap.items():
            bucket[v].append(k)

        bucket = [e for elem in bucket for e in elem]

        return bucket[-k+1:]