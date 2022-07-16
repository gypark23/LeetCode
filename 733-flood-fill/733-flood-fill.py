from collections import deque
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        queue = deque()
        row, col = len(image), len(image[0])
        visited = [[False] * col for i in range(row)]
        o_col = image[sr][sc]
        queue.append((sr, sc))
        
        while queue:
            r, c = queue.popleft()
            visited[r][c] = True
            if image[r][c] == o_col:
                image[r][c] = color
                for x, y in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                    new_r, new_c = r + x, c + y
                    if new_r in range(row) and new_c in range(col) and not visited[new_r][new_c]:
                        queue.append((new_r, new_c))
        
        return image
        
        