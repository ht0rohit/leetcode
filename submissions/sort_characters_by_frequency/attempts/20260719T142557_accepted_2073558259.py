class Solution:
    def frequencySort(self, s: str) -> str:
        frequency = {}
        for elem in s:
            if elem in frequency:
                frequency[elem] += 1
            else:
                frequency[elem] = 1

        bucket = [[] for _ in range(len(s) + 1)]
        for elem, freq in frequency.items():
            bucket[freq].append(elem)
        
        res = []
        for i in range(len(s), -1, -1):
            for elem in bucket[i]:
                res.append(elem * i)

        return "".join(res)