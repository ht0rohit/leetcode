class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        l = len(asteroids)
        st = []
        for i in range(l):
            flag = 0
            if not st:
                st.append(asteroids[i])
                continue
            
            if st[-1] > 0 and asteroids[i] > 0 or st[-1] < 0 and asteroids[i] < 0 or st[-1] < 0 and asteroids[i] > 0:
                st.append(asteroids[i])
                continue

            while st and st[-1] > 0 and asteroids[i] < 0:
                if abs(st[-1]) < abs(asteroids[i]):
                    st.pop()
                elif abs(st[-1]) == abs(asteroids[i]):
                    st.pop()
                    flag = 1
                    break
                else:
                    flag = 1
                    break
            if not flag:
                st.append(asteroids[i])

        return st
