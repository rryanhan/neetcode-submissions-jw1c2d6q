class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # makes a dict of items and occurrences
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)
        t = 0
        q = deque()

        while maxHeap or q:
            t += 1
            if maxHeap:
                task = heapq.heappop(maxHeap)
                task += 1
                # check if it is 0 or not
                if task != 0:
                    q.append([task, t + n])
            if q and q[0][1] == t:
                task, time = q.popleft()
                heapq.heappush(maxHeap, task)
        return t


        



# we need a maxHeap and a queue
# maxHeap stores the remaining amount
#  - tasks that are available to run right now
#  - priotize one with most remaining copies

# queue is items in cooldown
# [remaining_amount, time_when_available_again]

# how do we keep track of cooldown?