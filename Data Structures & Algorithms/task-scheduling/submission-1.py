class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)
        t = 0
        q = deque()

        while q or maxHeap:
            t += 1
            if maxHeap: # if there are immediate stuff we can process
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt, t + n])
            if q and q[0][1] == t:
                cnt, t = q.popleft()
                heapq.heappush(maxHeap, cnt)
        return t
