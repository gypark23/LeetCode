from collections import deque
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        row, col = len(mat), len(mat[0])
        ret = [[0] * col for i in range(row)]
        queue = deque()
        visited = set()
        for i in range(row):
            for j in range(col):
                if mat[i][j] == 0:
                    queue.append((i, j))
        
        level = 1
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        while(queue):
            size = len(queue)
            for _ in range(size):
                r, c = queue.popleft()
                for x, y in directions:
                    new_r, new_c = r + x, c + y
                    if new_r in range(row) and new_c in range(col) and (new_r, new_c) not in visited and mat[new_r][new_c] == 1:
                        queue.append((new_r, new_c))
                        visited.add((new_r, new_c))
                        ret[new_r][new_c] = level
            level += 1
                    
        return ret
        
        