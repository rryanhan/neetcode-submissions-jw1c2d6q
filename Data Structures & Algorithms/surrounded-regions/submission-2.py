class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS = len(board) 
        COLS = len(board[0])

        safe = set()

        def dfs(r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or (r, c) in safe or board[r][c] == "X":
                return
            safe.add((r, c))
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # first and last columns
        for i in range(ROWS):
            if board[i][0] == 'O':
                dfs(i, 0)
            if board[i][-1] == 'O':
                dfs(i, COLS - 1)

        # first and last rows
        for i in range(COLS):
            if board[0][i] == 'O':
                dfs(0, i)
            if board[-1][i] == 'O':
                dfs(ROWS - 1, i)
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in safe:
                    board[r][c] = "O"
                else:
                    board[r][c] = "X"
        
            
            
        

        
# which regions are NOT surrounded?
# traverse the borders, we can solve

# Any O that is on the border stays an O
# any other O that is not connected to those O's is turned into an x

# 1. mark border Os and Os connected to these border Os as safe
# 2. Turn the entire graph into Xs
# 3. Turn the safe tiles back into Os