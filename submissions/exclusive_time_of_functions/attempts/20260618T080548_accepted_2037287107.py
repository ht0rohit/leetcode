class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        stack = []
        hmap = {i:0 for i in range(n)}

        for i in range(len(logs)):
            log = logs[i].split(":")

            fun = int(log[0])
            call = log[1]
            time = int(log[2])

            if call == 'start':
                if stack and stack[-1][1] == 'start':
                    hmap[stack[-1][0]] += time - stack[-1][2]
                stack.append([fun, call, time])

            elif call == 'end':
                hmap[stack[-1][0]] += time - stack[-1][2] + 1
                stack.pop()
                if stack and stack[-1][1] == 'start':
                    stack[-1][2] = time + 1

        excl = []
        for i in range(n):
            excl.append(hmap[i])

        return excl
