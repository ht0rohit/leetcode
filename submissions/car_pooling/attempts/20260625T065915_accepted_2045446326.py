class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        from_i, to_i = {}, {}
        for elem in trips:
            if elem[1] in from_i:
                from_i[elem[1]] += elem[0]
            else:
                from_i[elem[1]] = elem[0]
            if elem[2] in to_i:
                to_i[elem[2]] += elem[0]
            else:
                to_i[elem[2]] = elem[0]

        for i in range(1000):
            if i in to_i:
                capacity += to_i[i]
            if i in from_i:
                if from_i[i] <= capacity:
                    capacity -= from_i[i]
                else:
                    return False
        
        return True