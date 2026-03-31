class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        count = 0
        ROWS, COLS = len(grid), len(grid[0])


        def bfs(r, c):
            q = deque()
            q.append((r, c))

            while q:
                r, c = q.popleft()
                if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == "0":
                    continue
                grid[r][c] = "0"
                for addR, addC in directions:
                    bfs(addR + r, addC + c)

            


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    bfs(r, c)
                    count += 1
        return count
        