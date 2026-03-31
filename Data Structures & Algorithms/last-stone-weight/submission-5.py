class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-stone for stone in stones]
        heapq.heapify(maxHeap)

        while maxHeap:
            x = heapq.heappop(maxHeap)
            if maxHeap:
                y = heapq.heappop(maxHeap)
            else:
                return x * -1
            newStone = abs((x * -1) - (y * -1))
            if newStone > 0:
                heapq.heappush(maxHeap, newStone * -1)
        return 0
            
        
        