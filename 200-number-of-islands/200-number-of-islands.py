from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ret = 0
        def dfs(grid, r, c):
            stack = deque()
            stack.append((r, c))
            directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
            
            while stack:
                new_r, new_c = stack.pop()
                grid[new_r][new_c] = "0"
                for x, y in directions:
                    new_r += x
                    new_c += y
                    if new_r in range(len(grid)) and new_c in range(len(grid[0])) and grid[new_r][new_c] == "1":
                        stack.append((new_r, new_c))
                    new_r -= x
                    new_c -= y
        
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    ret += 1
                    dfs(grid, r, c)
        
        return ret