class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        intervals = sorted(zip(startTime, endTime, profit))
        cache = {}

        def dfs(i):

            if i >= len(intervals):
                return 0

            if i in cache:
                return cache[i]

            #don't include
            res = dfs(i + 1)

            # include
            j = i + 1
            while j < len(intervals):
                # there is overlap
                if intervals[i][1] > intervals[j][0]:
                    j += 1
                else:
                    break
            res = max(res, intervals[i][2] + dfs(j))
            cache[i] = res
            return res


        return dfs(0)






# two options:
    # don't include the interval we are at
    # include it, and run dfs on the next available startTime we can find
        