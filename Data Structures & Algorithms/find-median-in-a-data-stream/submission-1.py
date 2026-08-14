class MedianFinder:

    def __init__(self):
        self.minHeap = []
            # THE LARGER HALF
        self.maxHeap = [] # in negatives, -1, -2, -3
            # THE SMALLER HALF
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.maxHeap, -num)
        
        # smallerHalf is larger, move it to larger half
        if self.maxHeap and self.minHeap and -self.maxHeap[0] > self.minHeap[0]:
            val = heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, -val)
        if len(self.maxHeap) - len(self.minHeap) > 1:
            val = heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, -val)
        elif len(self.minHeap) > len(self.maxHeap):
            val = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, -val)

        
    def findMedian(self) -> float:
        if len(self.maxHeap) == len(self.minHeap):
            val1, val2 = -self.maxHeap[0], self.minHeap[0]
            return (val1 + val2)/2
        else:
            return -self.maxHeap[0]

        
        