class Solution:
    def maximumWidth(self, planks: list[int]) -> int:
        cnt = Counter(planks)
        values = sorted(cnt)

        # Generate only achievable fence heights
        candidates = set(values)
        m = len(values)
        for i in range(m):
            for j in range(i, m):
                candidates.add(values[i] + values[j])

        ans = 0

        for H in candidates:
            width = cnt[H]

            for a in values:
                if a * 2 > H:
                    break

                b = H - a
                if b not in cnt:
                    continue

                if a == b:
                    width += cnt[a] // 2
                else:
                    width += min(cnt[a], cnt[b])

            ans = max(ans, width)

        return ans
