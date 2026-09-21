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
            value_elem = frequency.get(elem, None)
            if value_elem:
                palindrome = elem[1] + elem[0]
                value_palindrome = frequency.get(palindrome, None)
                if value_palindrome:
                    if elem != palindrome:
                        count += min(value_elem, value_palindrome) * 4
                        frequency[palindrome] -= value_palindrome
                        if frequency[palindrome] <= 0:
                            frequency[palindrome] = None
                    else:
                        if value_palindrome % 2 != 0:
                            flag = 1
                            duplicate += value_palindrome - 1
                        else:
                            count += value_palindrome * 2
                            frequency[elem] -= value_palindrome
                            if frequency[elem] <= 0:
                                frequency[elem] = None
            
        if duplicate or flag == 1:
            count += (duplicate + 1) * 2

        return count
