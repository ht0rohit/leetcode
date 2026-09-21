class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = {elem1: elem2 for elem1, elem2 in zip(position, speed)}
        cars = dict(sorted(cars.items()))
        
        st = []
        for p, s in cars.items():

            time = (target - p) / s
            while st and st[-1] <= time:
                st.pop()

            st.append(time)


        return len(st)