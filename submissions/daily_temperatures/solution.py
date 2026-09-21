class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        l = len(temperatures)
        if l == 1:
            return 0
        answer = [0] * l
        st = [0]

        for i in range(1, l):
            while st and temperatures[st[-1]] < temperatures[i]:
                answer[st[-1]] = i - st[-1]
                st.pop()
            st.append(i)

        return answer