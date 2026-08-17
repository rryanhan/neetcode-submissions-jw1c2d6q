class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        available = [i for i in range(n)]
        used = [] # end_time, room_number
        res = [0] * n

        for start, end in meetings:
            # first, free up all rooms
            while used and start >= used[0][0]:
                _, room_number = heapq.heappop(used)
                heapq.heappush(available, room_number)

            if available:
                available_room = heapq.heappop(available)
                res[available_room] += 1
                heapq.heappush(used, [end, available_room])
            
            else: # no rooms available
            # room is NOT available
                # take earliest end_time, delay it, move to available
                end_time, room_number = heapq.heappop(used)
                delay_time =  end - start
                new_end_time = end_time + delay_time
                heapq.heappush(used, [new_end_time, room_number])
                res[room_number] += 1
            # You are not changing or delaying the meeting currently occupying the room. That meeting keeps its existing end time. You are scheduling the new meeting to begin as soon as that room becomes available.
        return res.index(max(res))

        



# 5, 10
# 6, 12

# 0  1  2  3  4
# <----->
#    <-------->

# available rooms -> smallest room number first
# busy rooms -> earliest ending time first
    # end_time, room_#

# free EVERY toom whose meeting has ended by start

# then, we have two cases:
    # 1. room is available
        # take the smallest room, it runs at its original time
    # 2. room is NOT available
        # use the room that is closest to being free
        # delay it so it starts at end time
        # mark it as available, and use the delayed end time when we push it into the used heap
        