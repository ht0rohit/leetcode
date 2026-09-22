class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        m, n = len(s), len(t)

        if abs(m - n) > 1:
            return False

        def match(s, t, m, n):
            j = 0
            flag = False

            for i in range(m):
                if j == n:
                    return not flag

                if s[i] == t[j]:
                    j += 1
                elif not flag:
                    flag = True
                    if m == n:
                        j += 1
                else:
                    return False

            return flag or m != n

        if m >= n:
            return match(s, t, m, n)
        return match(t, s, n, m)