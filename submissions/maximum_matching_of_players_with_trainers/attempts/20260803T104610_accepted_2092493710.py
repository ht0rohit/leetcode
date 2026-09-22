class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        m, n = len(players), len(trainers)
        players.sort()
        trainers.sort()

        res = 0
        i, j = 0, 0
        while i < m and j < n:
            if trainers[j] >= players[i]:
                res += 1
                i += 1
                j += 1
            else:
                j += 1

        return res
