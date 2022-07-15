from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ret = 0
        queue = deque()
        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    ret += 1
                    queue.append((r, c))
                    
                    while queue:
                        new_r, new_c = queue.popleft()
                        for x, y in directions:
                            if new_r + x in range(len(grid)) and new_c + y in range(len(grid[0])) and grid[new_r + x][new_c + y] == "1":
                                queue.append((new_r + x, new_c + y))
                                grid[new_r + x][new_c + y] = "0"
        
        return ret
                    
        
        
        