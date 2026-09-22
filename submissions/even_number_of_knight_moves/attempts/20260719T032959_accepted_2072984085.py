class Solution:
    def canReach(self, start: list[int], target: list[int]) -> bool:
        # start at [0, 3]
        # target [4, 3] - 2 moves
        # Valid testcase
        
        return (start[0] + start[1]) % 2 == (target[0] + target[1]) % 2