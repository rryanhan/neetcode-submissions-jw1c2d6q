class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        q = deque()
        count = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append([r, c])
        
        while q:
            count += 1
            for _ in range(len(q)):
                r, c = q.popleft()
                for qr, qc in directions:
                    dr, dc = r + qr, c + qc
                    if dr < 0 or dc < 0 or dr >= ROWS or dc >= COLS or grid[dr][dc] != 2147483647:
                        continue
                    grid[dr][dc] = count
                    q.append([dr, dc])
                    


        

# mark 0s first
# from 0s, run bfs. replace value with count
# add to a set - if they have been visited already skip
#  ^ WAIT we dont need a set just see if it is equal to infinity

