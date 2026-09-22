class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        l1, l2 = len(s), len(goal)
        if l1 != l2:
            return False
        
        rotation = []
        for i in range(l1):
            if s[i] == goal[0]:
                rotation.append(i)

        flag = False
        for elem in rotation:
            i, j = elem, 0
            while j < l2:
                if s[i % l1] != goal[j]:
                    flag = False
                    break
                i += 1
                j += 1
            else:
                flag = True
                break

        return flag