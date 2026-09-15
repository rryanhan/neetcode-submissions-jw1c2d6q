"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda i : i.start)
        count = 1

        minHeap = []
        heapq.heappush(minHeap, intervals[0].end)

        for i in range(1, len(intervals)):
            startTime, endTime = intervals[i].start, intervals[i].end

            if startTime >= minHeap[0]:
                heapq.heappop(minHeap)
            else:
                count += 1
            heapq.heappush(minHeap, endTime)
        return count
        