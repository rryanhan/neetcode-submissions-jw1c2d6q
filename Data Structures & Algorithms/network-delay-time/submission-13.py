class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for source, target, t in times:
            adj[source].append([t, target])
        
        minHeap = [[0, k]]
        visited = set()
        res = 0

        while minHeap:
            cost, target = heapq.heappop(minHeap)
            if target in visited:
                continue

            
            res = cost
            visited.add(target)
            for c, nei in adj[target]:
                heapq.heappush(minHeap, [cost + c, nei])

        if len(visited) == n:
            return res

        return -1
        
        





# adjacency 
        