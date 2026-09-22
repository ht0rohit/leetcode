# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        people = set(range(n))

        i = 0
        for j in range(n):
            if i != j:
                res = knows(i, j)
                if res:
                    people.discard(i)
                if not res:
                    people.discard(j)

        if not people:
            return -1

        celeb = people.pop()
        for i in range(n):
            if i != celeb:
                res = knows(i, celeb)
                if not res:
                    return -1

        for j in range(n):
            if j != celeb:
                res = knows(celeb, j)
                if res:
                    return -1

        return celeb
