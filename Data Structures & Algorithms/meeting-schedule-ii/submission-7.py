"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        minHeap = []
        if not intervals:
            return 0
        intervals.sort(key=lambda i : i.start)
        heapq.heappush(minHeap, intervals[0].end)

        for i in range(1, len(intervals)):
            endTime = minHeap[0]
            # no overlap
            if endTime <= intervals[i].start:
                heapq.heappop(minHeap)
            heapq.heappush(minHeap, intervals[i].end)
        return len(minHeap)


# minHeap to track endtimes - goes from earliest endtime
# minHeap represents the rooms currently being used
# - smallest end time at the top of the heap is the room that frees up earliest

# case 1:
# - if start time >= earliest end time, that room is new free
# - we can pop it out of the heap, and reuse the room

# whether the room is reused, we need to place the current meeting somewhere
# - push it to the heap


# sort by start time, and use a minHeap. this ensures we are always matching the earliest start time with the earliest room that is free
# so if there is no overlap, we can use that room so we update it by popping from minHeap and using the new endTime
# if there is an overlap, we will need to use a new room for the new endTime


#        res = 1
#        intervals.sort(key=lambda i : i.start)
#        if not intervals:
#            return 0
#        lastEnd = intervals[0].end
#
#        for i in range(1, len(intervals)):
#            if lastEnd > intervals[i].start:
#                res += 1
#                lastEnd = min(intervals[i].end, lastEnd)
#                print(intervals[i].start)
#            else:
#                lastEnd = intervals[i].end
#        return res        


#              <----->
#     <---->
# <----------------------------------------->
# 0    5   10   15   20   25   30    35    40

# every time we overlap, we add a room
# set to max of the 2 intervals
# increment count by 1