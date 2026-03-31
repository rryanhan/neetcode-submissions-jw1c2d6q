class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)

        # { node : [target, cost] }
        for node, target, cost in times:
            adj[node].append([target, cost])

        # make minHeap [(cost, node)]
        minHeap = [(0, k)]

        # t keeps track of the cheapest path to hit all nodes
        t = 0

        # set makes sure we don't add duplicates
        visit = set()

        while minHeap:
            cost, node = heapq.heappop(minHeap)
            # The same node can be pushed into the heap multiple times 
            # with different costs.
            if node in visit: continue
            t = max(t, cost)
            visit.add(node)

            for nei, neiCost in adj[node]:
                heapq.heappush(minHeap, (cost + neiCost, nei))
        return t if len(visit) == n else -1


# need a minHeap to keep track of costs to get to node
# need to build an adjacency list
# need a set to make sure we visit only once


# how do we traverse the graph?
#  - while minHeap still has items

# 1. process the node, add to set
# 2. run for loop on neighbors, see if they're in set
#    add minHeap with the neighbour + current cost