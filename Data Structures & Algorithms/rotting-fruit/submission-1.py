class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        fruitCount = 0
        time = 0
        q = deque()
        directions = [[0, +1], [0, -1], [+1, 0], [-1, 0]]

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append([r, c])    
                if grid[r][c] == 1:
                    fruitCount += 1
        
        while fruitCount > 0 and q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if (row < 0 or col < 0 or row >= ROWS or col >= COLS or grid[row][col] == 0 or grid[row][col] == 2):
                        continue
                    grid[row][col] = 2
                    q.append((row, col))
                    fruitCount -= 1
            time += 1
        return time if fruitCount <= 0 else -1
            





# each time a bfs loop ends, that is t += 1
# we want to count how many fresh fruit there are
#  - every time we change a fresh fruit to a rotten fruit, we decrement
# if the number of fresh fruit is >0, we return -1 and not t