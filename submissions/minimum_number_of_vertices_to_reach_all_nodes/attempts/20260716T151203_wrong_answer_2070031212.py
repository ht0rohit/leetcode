class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        visited = set()
        res = []

        for elem in edges:
            if elem[0] not in visited:
                visited.add(elem[0])
                res.append(elem[0])
            if not elem[1] in visited:
                visited.add(elem[1])

        return res