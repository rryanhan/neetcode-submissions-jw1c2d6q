class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        res = []
        res.append(intervals[0])
        count = 0

        for i in range(1, len(intervals)):
            # if there is overlap:
            if res[-1][1] > intervals[i][0]:
                count += 1
                res[-1][1] = min(res[-1][1], intervals[i][1])

            # no overlap:
            else:
                res.append(intervals[i])
        return count

        
        



#      <----->
#  <--------->
#  <--->
#   1  2  3  4

# if there is an overlap, 
# we += 1 and update the interval?