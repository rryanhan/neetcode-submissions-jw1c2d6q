class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # tasks = {X : 2, Y : 2}

        # heap for active tasks we can push out

        # queue to keep track of cooldown

        count = Counter(tasks)
        
        heap = [-cnt for cnt in count.values()]
        heapq.heapify(heap)

        q = deque()

        time = 0

        while heap or q:
            # if we have item in heap, popleft, add the next time it is available into q
            #   - also decrement count, and dont add to queue if count becomes 0

            # if the first item in q is ready to process, remove and put it into heap
            if heap:
                task = heapq.heappop(heap)
                task += 1
                if task != 0:
                    q.append([task, time + n])
            if q and q[0][1] == time:
                queuedTask, time = q.popleft()
                heapq.heappush(heap, queuedTask)
            time += 1
        return time


        