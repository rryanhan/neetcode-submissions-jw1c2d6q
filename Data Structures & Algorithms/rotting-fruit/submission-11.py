class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        

    
    # multi source BFS

    # 1. start by identifying all of the fruits
    #   - get location, and get count

    # 2. start ms BFS
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        fruitCount = 0
        queue = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fruitCount += 1
                if grid[r][c] == 2:
                    queue.append([r, c])
        time = 0
        # while queue:
        while queue:
            if fruitCount == 0:
                return time

            for _ in range(len(queue)):
                row, col = queue.popleft()
                for r, c in directions:
                    dr, dc = row + r, col + c

                    if dr >= 0 and dc >= 0 and dr < ROWS and dc < COLS and grid[dr][dc] == 1:
                        fruitCount -= 1
                        grid[dr][dc] = 2
                        queue.append([dr, dc])
            time += 1
        if fruitCount != 0:
            return -1
        return time






