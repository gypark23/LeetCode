class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row, col = len(board), len(board[0])
        
        def dfs(r, c, w, visited):
            if not w:
                return True
            
            if board[r][c] != w[0]:
                return False
            
            if len(w) == 1:
                return True
            
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            w = w[1:]
            for x, y in directions:
                new_r, new_c = r + x, c + y
                if new_r in range(row) and new_c in range(col) and (new_r, new_c) not in visited:
                    visited.add((new_r, new_c))
                    if dfs(new_r, new_c, w, visited):
                        return True
                    else:
                        visited.remove((new_r, new_c))
            
            return False
        
        for i in range(row):
            for j in range(col):
                visited = set()
                visited.add((i, j))
                if dfs(i, j, word, visited):
                    return True
        
        return False
            