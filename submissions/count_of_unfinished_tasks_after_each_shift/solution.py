class Solution:
    def countTasks(self, tasks: List[int], shifts: List[int]) -> List[int]:
        prefix = []
        s = 0
        for x in tasks:
            s += x
            prefix.append(s)

        total = s
        processed = 0
        ans = []

        for t in shifts:
            processed += t

            if processed >= total:
                ans.append(0)
                processed = 0
            else:
                idx = bisect_right(prefix, processed)
                ans.append(len(tasks) - idx)

        return ans
        