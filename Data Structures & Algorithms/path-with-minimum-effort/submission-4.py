class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        ROWS, COLS = len(heights), len(heights[0])
        heap = []
        heapq.heappush(heap, (0, 0, 0)) # lowest effort, r, c
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        res = 99999999
        visited = set()

        while heap:
            minCost, r, c = heapq.heappop(heap)
            if r == ROWS - 1 and c == COLS - 1:
                return minCost
            if (r, c) in visited:
                continue
                
            visited.add((r, c))
            for dr, dc in directions:
                row, col = dr + r, dc + c
                if row < 0 or col < 0 or row >= ROWS or col >= COLS:
                    continue
                heapq.heappush(heap, (max(minCost, abs(heights[row][col] - heights[r][c])), row, col))

        return res

        

# just take the cheapest