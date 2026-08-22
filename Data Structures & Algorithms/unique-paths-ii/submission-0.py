class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ROWS, COLS = len(obstacleGrid), len(obstacleGrid[0])
        res = [0] * COLS
        # res represents the row below the current one, after all iterations this will become the top row
        for r in range(ROWS - 1, -1, -1):
            newRow = [0] * COLS
            for c in range(COLS - 1, -1, -1):
                # if grid == 1, zero ways
                if obstacleGrid[r][c] == 1:
                    newRow[c] = 0
                elif r == ROWS - 1 and c == COLS - 1:
                    newRow[c] = 1

                # add bottom and right if they are in-bounds
                else:
                    waysDown = res[c] 
                    waysRight = newRow[c + 1] if c + 1 < COLS else 0
                    newRow[c] = waysDown + waysRight

            res = newRow
        return res[0]

    
        