class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        hashmap = {}
        for elem in s:
            if elem in hashmap:
                hashmap[elem] += 1
            else:
                hashmap[elem] = 1

        for elem in t:
            if elem in hashmap:
                hashmap[elem] -= 1
            else:
                return False

        for k, v in hashmap.items():
            if v != 0:
                return False
        else:
            return True