class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime = sorted(processorTime)
        tasks = sorted(tasks, reverse=True)

        res = -1
        for i, j in enumerate(range(0, len(tasks), 4)):
            maxtime = processorTime[i] + tasks[j]
            if maxtime > res:
                res = maxtime

        return res