class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)

        for node, dest, cost in times:
            adj[node].append([cost, dest])
        minHeap = [(0, k)]

        visit = set()
        t = 0

        while minHeap:
            cost, node = heapq.heappop(minHeap)
            if node in visit:
                continue
            t = max(cost, t)
            for neiCost, neiDest in adj[node]:
                if neiDest in visit:
                    continue
                heapq.heappush(minHeap, (cost + neiCost, neiDest))
            visit.add(node)
        return t if len(visit) == n else -1



        




# minHeap to keep track of the costs up to now
# minHeap = [cost,  node]

# we need an adjacency matrix; adj[n]= [node, pathCost]
# we need a visit set
# we need a t variable that expands the min cost to hit all nodes