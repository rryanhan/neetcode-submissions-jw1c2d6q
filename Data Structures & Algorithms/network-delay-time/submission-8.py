class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for src, tar, ti in times:
            adj[src].append([tar, ti])

        minHeap = [(0, k)]
        heapq.heapify(minHeap)

        res = 0

        visited = set()

        while minHeap:
            cost, node = heapq.heappop(minHeap)

           #if node == n:
            #    return res

            if node in visited:
                continue
            
            visited.add(node)

            # we need to append neighbours and update their costs
            # also need to update 

            res = max(cost, res)

            for nei, neiCost in adj[node]:
                heapq.heappush(minHeap, (neiCost + cost, nei))
            
        return res if len(visited) == n else -1





# adj = { node : [[neighbour, cost ]]}

# set to keep track of nodes we have visited on this path
# minHeap : [cost to get to this node, the node]