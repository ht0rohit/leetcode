class Solution:
    def numDecodings(self, s: str) -> int:
        l = len(s)

        num_ways = [0 if s[0] == '0' else 1] + [-1] * (l - 1)

        for i in range(1, l):
            if s[i] == '0':
                if s[i-1] < '3':
                    if i == 1:
                        num_ways[i] = num_ways[i-1]
                    else:
                        num_ways[i] = num_ways[i-1] - 1
                else:
                    return 0 
            
            elif s[i-1] != '0' and s[i-1] < '3':
                if s[i-1] == '2' and s[i] > '6':
                    num_ways[i] = num_ways[i-1]
                else:
                    num_ways[i] = num_ways[i-1] + 1

            else:
                num_ways[i] = num_ways[i-1]

        return num_ways[-1]