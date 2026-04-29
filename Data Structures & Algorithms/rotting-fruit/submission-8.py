class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS, = len(grid), len(grid[0])
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        fresh = 0
        time = 0
        q = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append([r, c])
                if grid[r][c] == 1:
                    fresh += 1

        while q and fresh != 0:
            for _ in range(len(q)):
                row, col = q.popleft()
                for r, c in directions:
                    dr, dc = row + r, col + c
                    if dr < 0 or dc < 0 or dr >= ROWS or dc >= COLS or grid[dr][dc] != 1:
                        continue
                    grid[dr][dc] = 2
                    q.append([dr, dc])
                    fresh -= 1
            time += 1
        if fresh != 0:
            return -1
        return time

        
        