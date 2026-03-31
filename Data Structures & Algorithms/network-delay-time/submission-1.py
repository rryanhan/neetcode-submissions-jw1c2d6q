class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = defaultdict(list)
        
        for u, v, w in times:
            edges[u].append((v, w)) #target, cost

        minHeap = [(0, k)]
        dic = [float("inf")] * (n + 1)
        dic[k] = 0
        
        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            
            for n2, w2 in edges[n1]:
                if dic[n2] > w1 + w2:
                    dic[n2] = w1 + w2
                    heapq.heappush(minHeap, (w1 + w2, n2))
                
        ans = dic[1:]
        return max(ans) if max(ans) < float("inf") else -1

