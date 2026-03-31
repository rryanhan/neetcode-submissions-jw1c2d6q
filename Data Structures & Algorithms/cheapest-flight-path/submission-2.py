import heapq
from collections import defaultdict

class Solution:
    def findCheapestPrice(self, n, flights, src, dst, k):
        graph = defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))

        # dist[node][flights_used]
        dist = [[float("inf")] * (k + 2) for _ in range(n)]
        dist[src][0] = 0

        heap = [(0, src, 0)]  # cost, node, flights_used

        while heap:
            cost, node, flights = heapq.heappop(heap)

            if node == dst:
                return cost

            if flights == k + 1:
                continue

            for nei, price in graph[node]:
                newCost = cost + price
                newFlights = flights + 1

                if newCost < dist[nei][newFlights]:
                    dist[nei][newFlights] = newCost
                    heapq.heappush(heap, (newCost, nei, newFlights))

        return -1