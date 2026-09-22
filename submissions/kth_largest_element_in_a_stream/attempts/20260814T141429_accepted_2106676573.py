class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.minheap = []

        for num in nums:
            _ = self.add(num)

    def add(self, val: int) -> int:
        if len(self.minheap) < self.k:
            heapq.heappush(self.minheap, val)
        elif self.minheap[0] < val:
            heapq.heappop(self.minheap)
            heapq.heappush(self.minheap, val)
        
        return self.minheap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)