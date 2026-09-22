class Solution:
    def frequencySort(self, s: str) -> str:
        frequency = {}
        for elem in s:
            if elem in frequency:
                frequency[elem] += 1
            else:
                frequency[elem] = 1

        frequency = dict(sorted(frequency.items(), key=lambda item: item[1], reverse=True))
        
        res = ""
        for key, value in frequency.items():
            res += key * value

        return res