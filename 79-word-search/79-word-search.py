class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row, col = len(board), len(board[0])
        row_s = set(range(row))
        col_s = set(range(col))
        visited = set()
        def dfs(r, c, i):
            if i >= len(word):
                return True
            
            if r not in row_s or c not in col_s or (r, c) in visited or board[r][c] != word[i]:
                return False
            
            visited.add((r, c))
            
            ret = dfs(r + 1, c, i + 1) or dfs(r, c + 1, i + 1) or dfs(r - 1, c, i + 1) or dfs(r, c - 1, i + 1)
            
            visited.remove((r, c))
            
            return ret
        
        for i in range(row):
            for j in range(col):
                if dfs(i, j, 0):
                    return True
        
        return False