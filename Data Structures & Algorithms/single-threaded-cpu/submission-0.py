class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        time = 0
        minHeap = []
        for i, t in enumerate(tasks):
            heapq.heappush(minHeap, [t[0], t[1], i])

        completed = [False] * len(tasks)
        picker = []
        res = []

        while minHeap or picker:
            while minHeap and minHeap[0][0] <= time:
                eTime, pTime, index = heapq.heappop(minHeap)
                heapq.heappush(picker, [pTime, index, eTime])
            if picker:
                pTime, i, eTime = heapq.heappop(picker)
                time += pTime
                res.append(i)

            else:
                time += 1
        return res
            




# condition:
    # is enqueueTime <= time?
        
# sometimes, we can have more than one task available
    # say processingTime takes t from 0 to 4, and we have eT at 1 and 2