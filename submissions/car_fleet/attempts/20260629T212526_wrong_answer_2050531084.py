class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        l = len(position)
        cars = {elem1: ((target - elem1) / elem2) for elem1, elem2 in zip(position, speed)}
        cars = dict(sorted(cars.items()))
        st = []

        fleet = 0
        for k, v in cars.items():
            if not st:
                st.append(v)
                continue

            if st and st[-1] > v:
                while st and st[-1] > v:
                    st.pop()
                st.append(v)
                fleet += 1
            else:
                st.append(v)
        
        fleet += 1
        return fleet
            