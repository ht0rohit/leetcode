class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change = {5: 0, 10: 0}
        for elem in bills:
            if elem == 5:
                change[5] += 1
                continue
            elif elem == 10:
                if change[5] > 0:
                    change[5] -= 1
                    change[10] += 1
                    continue
                else:
                    break
            elif elem == 20:
                if change[10] > 0:
                    change[10] -= 1
                    if change[5] > 0:
                        change[5] -= 1
                        continue
                    else:
                        break
                elif change[5] > 2:
                    change[5] -= 3
                    continue
                else:
                    break
        else:
            return True
        
        return False

