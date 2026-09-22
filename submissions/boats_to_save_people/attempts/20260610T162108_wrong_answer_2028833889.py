class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        i, boats, cur_weight = 0, 0, 0
        while i < len(people):
            if cur_weight + people[i] < limit:
                if i != len(people) - 1:
                    cur_weight += people[i]
                    i += 1
                else:
                    boats += 1
                    i += 1    
            elif cur_weight + people[i] == limit:
                cur_weight = 0
                boats += 1
                i += 1
            elif cur_weight + people[i] > limit:
                cur_weight = 0
                boats += 1
            else:
                pass

        return boats