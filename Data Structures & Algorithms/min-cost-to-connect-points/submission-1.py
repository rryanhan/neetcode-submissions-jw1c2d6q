class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # { this_point : [other_connecting_point, distance]}
        adj = { i : [] for i in range(len(points))}

        for i in range(len(points) - 1):
            x1, y1 = points[i]
            for j in range(i + 1, len(points)):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append([j, dist])
                adj[j].append([i, dist])
        cost = 0

        # (dist, node)
        minHeap = [[0, 0]]
        visit = set()

        while len(visit) < len(points):
            dist, node = heapq.heappop(minHeap)
            # check if processed; skip if yes
            if node in visit:
                continue

            # add this node to visit
            # add the distance to cost
            visit.add(node)
            cost += dist

            # add all its neighbours to minHeap
            for neiNode, neiDist in adj[node]:
                if neiNode in visit:
                    continue
                heapq.heappush(minHeap, [neiDist, neiNode])
        return cost


        



# can we just get smallest point
# adjacency list of every point connecting to every other point
# use minHeap to get lowest cost connect

# go through points
# connect with minHeap, add point to set

# how do we build the graph?
#  - double for 


