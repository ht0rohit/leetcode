class Solution:
    def minBuildTime(self, blocks: List[int], split: int) -> int:
        heapq.heapify(blocks)

        while len(blocks) > 1:            
            # Pop two minimum. The time of the abstracted sub-root will be 
            # split + max(x, y) which is split + y
            x = heapq.heappop(blocks)
            y = heapq.heappop(blocks)
            heapq.heappush(blocks, split + y)

        # Time of final root node
        return heapq.heappop(blocks)
