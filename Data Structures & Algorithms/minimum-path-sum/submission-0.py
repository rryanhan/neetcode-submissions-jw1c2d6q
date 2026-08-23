class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        res = [float("inf")] * COLS 

        for r in range(ROWS - 1, -1, -1):
            currRow = [0] * COLS
            for c in range(COLS - 1, -1, -1):
                if r == ROWS - 1 and c == COLS - 1:
                    currRow[c] = grid[r][c]
                    continue
                valueRight = currRow[c + 1] if c + 1 < COLS else float("inf")
                valueDown = res[c]
                currRow[c] = grid[r][c] + min(valueRight, valueDown)
            res = currRow
        return res[0]
                


# dp = len(grid) -> by row

# go bottom row -> top row
    # go right col -> left col

    # dp[i] = minimum path from this column for the row that we are currently on
        
