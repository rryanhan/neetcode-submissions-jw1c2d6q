class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        freshCount = 0
        visited = set()

        ROWS, COLS = len(grid), len(grid[0])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    freshCount += 1
                if grid[r][c] == 2: 
                    q.append([r, c])

        time = 0
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        while q and freshCount != 0:
            for _ in range(len(q)):
                r, c = q.popleft()
                for row, col in directions:
                    dr, dc = row + r, col + c
                    if dr < 0 or dc < 0 or dr >= ROWS or dc >= COLS or grid[dr][dc] != 1:
                        continue
                    grid[dr][dc] = 2
                    q.append([dr, dc])
                    freshCount -= 1
                    


            time += 1
        return time if freshCount == 0 else -1

        