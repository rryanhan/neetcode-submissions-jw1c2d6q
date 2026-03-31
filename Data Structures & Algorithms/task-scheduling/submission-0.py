class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # there is a maxHeap and a queue
        # maxHeap tracks: occurrences of a task we need to process; most to least
        # queue will track occurences of that task remaining with its cooldown time
        # if cooldown time == time on the queue, we can move it back into maxHeap
        # we increment time by 1 if there are available tasks to process, or stuff in cooldown

        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        q = deque()

        time = 0
        while maxHeap or q:
            time += 1
            if maxHeap: #pop, decrement, add to queue
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt != 0:
                    q.append([cnt, time + n]) # [0, 1, 2, 3] n = 2, A -> A is next ready at 3
            # if there is a matching q, add it to maxHeap
            if q and q[0][1] == time:
                cnt, t = q.popleft()
                heapq.heappush(maxHeap, cnt)
        return time


