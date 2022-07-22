class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ret = []
        diag = set()
        antidiag = set()
        col = set()
        
        def backtrack(row, board):
            if row >= n:
                ret.append(board[:])
                return
        
            for c in range(n):
                #can't because it's diagonal
                if row + c in diag or row - c in antidiag or c in col:
                    continue
                
                #valid placement
                string = list(board[row])
                string[c] = "Q"
                board[row] = "".join(string)
                
                #update col and unavailable
                col.add(c)
                diag.add(row + c)
                antidiag.add(row - c)
            
                backtrack(row + 1, board[:])
                board[row] = "." * n
                col.remove(c)
                diag.remove(row + c)
                antidiag.remove(row - c)
        
        board = ["." * n for i in range(n)]
        backtrack(0, board)
        
        return ret