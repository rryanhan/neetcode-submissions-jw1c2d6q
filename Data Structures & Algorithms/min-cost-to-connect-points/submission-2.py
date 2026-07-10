class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = { i : [] for i in range(len(points))}

        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                xi, yi = points[i]
                xj, yj = points[j]
                manDistance = abs(xi - xj) + abs(yi - yj)
                adj[i].append([j, manDistance])
                adj[j].append([i, manDistance])
        
        res = 0

        minHeap = [[0, 0]]
        visited = set()
        
        while len(visited) != len(points):
            distance, node = heapq.heappop(minHeap)
            if node in visited:
                continue
            visited.add(node)
            res += distance
            for nei, cost in adj[node]:
                heapq.heappush(minHeap, [cost, nei])
        return res

        




# build graph, two way connection between every node
# calculate manhattan distance

# set up a minHeap -> how do we set this up? 
    # what is th first value?


# for x, y in points:?? what is the condition
    # see if nodes have beenn visited already
    # connect with the cheapest neighbour


