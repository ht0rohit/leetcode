class Solution:
    def numDecodings(self, s: str) -> int:
        l = len(s)
        s = '1' + s

        num_ways = [1] + [0 if s[1] == '0' else 1] + [0] * (l - 1)

        for i in range(2, l + 1):
            if s[i] == '0':
                if s[i-1] == '0':
                    return 0
                elif s[i-1] > '2':
                    return 0
                else:
                    num_ways[i] = num_ways[i-2]
            else:
                if s[i-1] == '0':
                    num_ways[i] = num_ways[i-1]
                elif s[i-1] > '2' or (s[i] > '6' and s[i-1] > '1'):
                    num_ways[i] = num_ways[i-1]
                else:
                    num_ways[i] = num_ways[i-1] + num_ways[i-2]

        return num_ways[-1]