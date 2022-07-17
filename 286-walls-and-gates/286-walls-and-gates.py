from collections import deque

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        row, col = len(rooms), len(rooms[0])
        #visited = set()
        queue = deque()
        
        for i in range(row):
            for j in range(col):
                if rooms[i][j] == 0:
                    queue.append((i, j))
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        level = 1
        while queue:
            size = len(queue)
            for _ in range(size):
                r, c = queue.popleft()
                for x, y in directions:
                    new_r, new_c = r + x, c + y
                    if new_r in range(row) and new_c in range(col) and  rooms[new_r][new_c] == 2147483647:
                        rooms[new_r][new_c] = level
                        #visited.add((new_r, new_c))
                        queue.append((new_r, new_c))
            level += 1
        
        return rooms
            
        