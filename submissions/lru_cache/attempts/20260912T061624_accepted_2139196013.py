# Python dictionaries preserve insertion order, so effectively
# Finding first element with next(iter(...)) → O(1)
# If language-independent canonical solution is expected
# Use hashmap + doubly linked list (DLL) structure instead.

class LRUCache:

    def __init__(self, capacity: int):
        # Store key: value, updated index
        self.hmap1 = {}
        # Store updated index: key
        self.hmap2 = {}
        # Max len of hmap
        self.capacity = capacity
        # Last used index
        self.lui = 0

    def get(self, key: int) -> int:
        # Update lui if key is found
        if key in self.hmap1:
            res = self.hmap1[key]
            ind = res[1]
            self.lui += 1
            self.hmap1[key][1] = self.lui
            # Evict key with stale lui and create new one 
            del self.hmap2[ind]
            self.hmap2[self.lui] = key
            return res[0]

        # Simply return if key not found
        return -1

    def put(self, key: int, value: int) -> None:
        # Update key value and perform get op to update lui
        if key in self.hmap1:
            self.hmap1[key][0] = value
            _ = self.get(key)
            return

        # Evict lru elem from both dictionaries
        elif len(self.hmap2) == self.capacity:
            # Get key of 1st element of hmap2
            first_ind = next(iter(self.hmap2))
            first_key = self.hmap2[first_ind]
            # Delete 1st element of hmap2
            del self.hmap2[first_ind]
            # Delete the key from hmap1
            del self.hmap1[first_key]

        # Perform append operation len < capacity or lru is evicted
        self.lui += 1
        self.hmap1[key] = [value, self.lui]
        self.hmap2[self.lui] = key


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)