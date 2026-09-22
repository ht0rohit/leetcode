class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        pixel = image[sr][sc]
        if pixel == color:
            return image

        m, n = len(image), len(image[0])
        q = collections.deque()
        image[sr][sc] = color
        q.append((sr, sc))

        while q:
            r, c = q.popleft()
            if r - 1 >= 0 and image[r-1][c] == pixel:
                image[r-1][c] = color
                q.append((r-1, c))
            if c - 1 >= 0 and image[r][c-1] == pixel:
                image[r][c-1] = color
                q.append((r, c-1))
            if c + 1 < n and image[r][c+1] == pixel:
                image[r][c+1] = color
                q.append((r, c+1))
            if r + 1 < m and image[r+1][c] == pixel:
                image[r+1][c] = color
                q.append((r+1, c))

        return image