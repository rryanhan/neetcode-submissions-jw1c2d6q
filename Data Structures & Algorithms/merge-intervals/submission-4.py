class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        res = []
        if len(intervals) == 0:
            return res
        res.append(intervals[0])

        for i in range(1, len(intervals)):
            # case 1
            if res[-1][1] < intervals[i][0]:
                res.append(intervals[i])
            elif res[-1][1] >= intervals[i][0]:
                res[-1][1] = max(res[-1][1], intervals[i][1])

        return res




# what are the cases?
    # 1. intervals[-1][end] is before intervals[i][start]
        # NO overlap
        # simply append the intervals[i] to res
    # 2. intervals[-1][end] is after intervals[i][start]
        # there is overlap
        # need to update the intervals[-1][end] with the end time
        # of the new interval
            # -> not just the new one, the max of both endpooints
            # [1, 5] [2, 3]
            # -> becomes [1, 5] ; the max of the ends