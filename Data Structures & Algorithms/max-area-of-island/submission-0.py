class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        res = 0

        def dfs(row, col):
            # if out of bounds or island is 0, return
            # change current island from 1 to 0
            # if in bound, do dfs 4 ways, +1 current
            if row < 0 or col < 0 or row >= rows or col >= cols or grid[row][col] == 0:
                return 0
            grid[row][col] = 0
            
            return 1 + dfs(row + 1, col) + dfs(row - 1, col) + dfs(row, col + 1) + dfs(row, col - 1)



        for r in range(rows):
            for c in range(cols):
                # if we are at a 1, run dfs. after it runs, get the area and compare
                if grid[r][c] == 1:
                    finalArea = dfs(r, c)
                    res = max(finalArea, res)
        return res

