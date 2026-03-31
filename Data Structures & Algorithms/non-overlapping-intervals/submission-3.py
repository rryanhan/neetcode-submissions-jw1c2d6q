class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda i : i[0])
        res = 0
        arr = []
        arr.append(intervals[0])

        for i in range(1, len(intervals)):
            # if there is no overlap
            if intervals[i][0] >= arr[-1][1]:
                arr.append(intervals[i])
                continue
            else:
                res += 1
                arr[-1][1] = min(arr[-1][1], intervals[i][1])
        return res

#                              <--------------->
#                       <--------------->        
#              <--------------->
#        <-------------->
# <------------->
# 0      1      2       3       4       5      6      7


 
#         <--------------->
# <----------------------->
# <------->
#  1      2       3       4       5      6      7

# if merge, the prev end becomes min of the 2 that we merge, count up by 1