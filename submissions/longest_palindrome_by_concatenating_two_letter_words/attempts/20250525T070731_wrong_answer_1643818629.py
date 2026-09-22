class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        frequency = {}
        for elem in words:
            if elem in frequency:
                frequency[elem] += 1
            else:
                frequency[elem] = 1

        count = 0; flag = 0
        for elem in words:
            palindrome = elem[1] + elem[0]
            if elem != palindrome:
                if frequency.get(palindrome, None):
                    count += 4
                    frequency[elem] -= 1
                    if frequency[elem] <= 0:
                        frequency[elem] = None
                    frequency[palindrome] -= 1
                    if frequency[palindrome] <= 0:
                        frequency[palindrome] = None
            else:
                if frequency.get(palindrome, None):
                    if not flag:
                        flag = 1
                        count += 2
                        frequency[palindrome] -= 1
                        if frequency[palindrome] <= 0:
                            frequency[palindrome] = None

        return count