class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        frequency = {}
        for elem in words:
            if elem in frequency:
                frequency[elem] += 1
            else:
                frequency[elem] = 1

        count, flag = 0, 0
        value, duplicate = 0, 0
        for elem in frequency:
            palindrome = elem[1] + elem[0]
            if elem != palindrome:
                if frequency.get(palindrome, None):
                    count += 4
                    print(count)
                    frequency[elem] -= 1
                    if frequency[elem] <= 0:
                        frequency[elem] = None
                    frequency[palindrome] -= 1
                    if frequency[palindrome] <= 0:
                        frequency[palindrome] = None
            else:
                value = frequency.get(palindrome)
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
