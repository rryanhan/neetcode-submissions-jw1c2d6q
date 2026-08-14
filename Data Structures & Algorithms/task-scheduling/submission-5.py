class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        taskCount = Counter(tasks)

        heap = [-cnt for cnt in taskCount.values()]
        heapq.heapify(heap)

        q = deque()
        time = 0

        while heap or q:
            time += 1
            if q:
                if q[0][1] == time:
                    tasktoadd, availabletime = q.popleft()
                    heapq.heappush(heap, tasktoadd)

            if heap:
                task = heapq.heappop(heap)
                task += 1
                if task != 0:
                    q.append([task, time + n + 1])
            
            

        return time




        


# a max heap to keep track of tasks we need to process, sorted by most

# a queue that keeps track of tasks in cooldown and when they are next available