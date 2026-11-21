class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        ROWS, COLS = len(image), len(image[0])
        DIRS = ((0, -1), (0, 1), (1, 0), (-1, 0))
        old = image[sr][sc]

        q = collections.deque([(sr, sc)])
        visited = set()
        while q:
            r, c = q.popleft()
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or image[r][c] != old or (r, c) in visited:
                continue
            image[r][c] = color
            visited.add((r, c))
            for dr, dc in DIRS:
                q.append((r + dr, c + dc))
        
        return image
