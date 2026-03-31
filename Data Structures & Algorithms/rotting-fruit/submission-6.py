class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        res = 0
        q = deque()
        freshCount = 0
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append([r, c])
                if grid[r][c] == 1:
                    freshCount += 1
        
        if freshCount == 0:
            return 0

        while q:
            for _ in range(len(q)):
                row, col = q.popleft()
                for r, c in directions:
                    dr, dc = row + r, col + c
                    if dr < 0 or dc < 0 or dr >= ROWS or dc >= COLS or grid[dr][dc] == 2 or grid[dr][dc] == 0:
                        continue
                    else:
                        grid[dr][dc] = 2
                        q.append([dr, dc])
                        freshCount -= 1
            res += 1
            if freshCount == 0:
                return res
        return -1
            


        


# run bfs on rotten fruits 
# stop once we have covered all rotten fruits

# 1. go through the grid first to find the spots of the rotten fruits 
#    and add them to a queue. 
# 2. then run bfs using while q, for _ in range(len(queue)) 
#    which will let me go through it layer by later. 
# 3. once ive converted all the fruits, 
#    i return a variable like count or smt