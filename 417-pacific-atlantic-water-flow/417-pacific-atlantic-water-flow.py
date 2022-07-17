class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        row, col = len(heights), len(heights[0])
        def pacific(r, c):
            return (r == 0 and c in range(col)) or (c == 0 and r in range(row))
        def atlantic(r, c):
            return (r == row - 1 and c in range(col)) or (c == col - 1 and r in range(row))
        
        pacific_v, atlantic_v = set(), set()
        ret = []
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        def dfs(r, c, ocean):
            if (r, c) in ocean:
                return
            else:
                ocean.add((r, c))
            for x, y in directions:
                new_r, new_c = r + x, c + y
                if new_r in range(row) and new_c in range(col) and heights[r][c] <= heights[new_r][new_c]:
                    dfs(new_r, new_c, ocean)
        
        for i in range(row):
            for j in range(col):
                if pacific(i, j):
                    dfs(i, j, pacific_v)
                if atlantic(i, j):
                    dfs(i, j, atlantic_v)
        
        for r, c in pacific_v.intersection(atlantic_v):
            ret.append([r, c])
        return ret