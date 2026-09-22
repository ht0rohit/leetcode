class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        frequency = {}
        for elem in words:
            if elem in frequency:
                frequency[elem] += 1
            else:
                frequency[elem] = 1

        count = 0
        flag, duplicate = 0, 0
        for elem in frequency:
            if frequency.get(elem, None):
                palindrome = elem[1] + elem[0]
                value = frequency.get(palindrome, None)
                if elem != palindrome:
                    if value:
                        count += value * 4
                        frequency[palindrome] -= value
                        if frequency[palindrome] <= 0:
                            frequency[palindrome] = None
                else:
                    if value % 2 != 0:
                        flag = 1
                        duplicate += value - 1
                    else:
                        count += value * 2
                        frequency[elem] -= value
                        if frequency[elem] <= 0:
                            frequency[elem] = None
            
        if duplicate or flag == 1:
            count += (duplicate + 1) * 2

        return count
