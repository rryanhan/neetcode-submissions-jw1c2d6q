class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        
        for i in range(len(intervals)):
            # case 1: newInterval completely to the left
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            # case 2: newInterval completely to the right
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            # case 3: merge
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
        res.append(newInterval)
        return res
        


# 3 cases:
# 1. newInterval is completely to the left
#    - res.append(newInterval) + intervals[i:]
# 2. newInterval is completely to the right
#    - res.append(intervals[i])
#    - don't do anything to newInterval
# 3. there is an overlap
#    - we need to update newInterval, merging intervals[i] with newInterval
#    - dont append anything

# append newInterval at the end if we never do in the for loop

#        <----------------------->
#                       <---------------->   
# <-------------->
#  1      2       3       4       5      6