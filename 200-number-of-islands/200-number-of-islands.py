from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row, col = len(grid), len(grid[0])
        queue = deque()
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        ret = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1":
                    ret += 1
                    queue.append((i, j))
                    while queue:
                        r, c = queue.popleft()
                        grid[r][c] = "0"
                        for x, y in directions:
                            new_r, new_c = r + x, c + y
                            if new_r in range(row) and new_c in range(col) and grid[new_r][new_c] == "1":
                                queue.append((new_r, new_c))
                                grid[new_r][new_c] = "0"
        
        return ret
        