"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key = lambda i : i.start)
        minHeap = []
        if len(intervals) == 0:
            return 0
        heapq.heappush(minHeap, intervals[0].end)
        count = 1

        for i in range(1, len(intervals)):
            # meeting needs a new room
            if minHeap[0] > intervals[i].start:
                heapq.heappush(minHeap, intervals[i].end)
                count += 1
            else:
                endTime = heapq.heappop(minHeap)
                heapq.heappush(minHeap, intervals[i].end)
        return count


        


# number of rooms at the end is how many 


# use a minheap to get the room with the soonest next opening
    # so sort minHeap by end time?

# case 1:
    # meeting needs a new room
    # add to the minHeap
    # increase room count by 1

# case 2:
    # meeting does not need a new room
    # update the minHeap end time
    # keep the room count
