class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        hashmap = {'b': 0, 'a': 0, 'l': 0, 'o': 0, 'n': 0}
        for elem in text:
            if elem in hashmap:
                hashmap[elem] += 1
        
        res = min(hashmap.values())
        res = min(res, hashmap['l'] // 2, hashmap['o'] // 2)
        return res