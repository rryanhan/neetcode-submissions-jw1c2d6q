class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.sort()

        res = []

        for i in range(len(intervals)):
            # case 3 -> newInterval is COMPLETELY before
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                print(intervals[i])
                res += intervals[i:]
                return res
            # case 2 -> newInterval is completely after
            if intervals[i][1] < newInterval[0]:
                res.append(intervals[i])
            
            # case 3 -> overlap
            else:
                newInterval[0] = min(newInterval[0], intervals[i][0])
                newInterval[1] = max(newInterval[1], intervals[i][1])
#.               <-------->
#                     <------>
#             <----->
            # 1  2  3  4  5  6
            

        res.append(newInterval)
        return res




# what are the cases?
    # we have res[]

    # 1. if intervals[i][end] < newInterval[start]
        # NO overlap
        # we can just append intervals[i] to res

    # 2. if intervals[i][end] >= newInterval[start]
        # there IS overlap
        # do we update newInterval[start] with min?

    # 3. if intervals[i][start] > newInterval[end]
        # all of new interval comes before
        # append newInterval(?) to res
        # append rest of intervals to res