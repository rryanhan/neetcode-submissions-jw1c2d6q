class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        # count of how many times we've used
        used = [0] * n

        # minHeap of rooms that are available
        available = [i for i in range(n)] # always go for the lowest number room

        # minHeap of rooms that are used
        unavailable = [] # (when it ends, room number)

        for start, end in meetings:
            # pop all rooms that are being used that can now be freed
            while unavailable and unavailable[0][0] <= start:
                _, room_no = heapq.heappop(unavailable)
                heapq.heappush(available, room_no)

            # check if we have any available rooms, use that
            if available:
                room_no = heapq.heappop(available)
                heapq.heappush(unavailable, (end, room_no))
                used[room_no] += 1

            # if there are no available rooms, then use the unavailable room that will become available next, and delay it 
            else:
                end_time, room_no = heapq.heappop(unavailable)
                new_time = end_time + (end - start)
                heapq.heappush(unavailable, (new_time, room_no))
                used[room_no] += 1
        return used.index(max(used))



# <------>
#     <-------->