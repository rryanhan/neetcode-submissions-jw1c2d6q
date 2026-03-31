class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i : i[0])
        output = [intervals[0]]

        for start, end in intervals[1:]:
            lastEnd = output[-1][1]

            if start <= lastEnd:
                output[-1][1] = max(lastEnd, end)
            else:
                output.append([start, end])
        return output

#        res = []
#        mergeInterval = []
#        for i in range(len(intervals) - 1):
#            if intervals[i][1] < intervals[i + 1][0]:
#                res.append(intervals[i])
#            else:
#                mergeInterval = [min(intervals[i][0], intervals[i + 1][0]), max(intervals[i][1], intervals[i + 1][1])]


# if intervals[i][1] < intervals[i + 1][0]
# preceed as usual, append res.append(intervals[i])
# else:
# - newInterval = min(start_i_1, start_i_2), max(end_i_1, end_i_2)

# 
        