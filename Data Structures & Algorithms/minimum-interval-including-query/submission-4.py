class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        # way to map query answer to index
        mapping = {}
        heap = []

        i = 0

        for q in sorted(queries):
            while i < len(intervals) and intervals[i][0] <= q:
                heapq.heappush(heap, (intervals[i][1] - intervals[i][0] + 1, intervals[i][1]))
                i += 1
            while heap and heap[0][1] < q:
                heapq.heappop(heap)

            if heap:
                mapping[q] = heap[0][0]
            

        res = [-1] * len(queries)
        for index, number in enumerate(queries):
            if number in mapping:
                res[index] = mapping[number]
        return res








# sort queries
    # loop for queries
        # pop intervals that are out of range
        # for interval is within query, add: [length, end_time] into a minHeap
        

# ATTEMPT 2

# DONT for loop intervals, just one pass interval

# sort queries
    # while intervals could be within the range, add it to the heap

    # grab intervals from the heapl; if they're expired then pop them out

    # put in the shortest interval into the output
