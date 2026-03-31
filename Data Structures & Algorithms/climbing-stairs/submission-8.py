class Solution:
    def climbStairs(self, n: int) -> int:
        cache = [-1] * n

        def dfs(i):
            if i == n:
                return 1
            if i > n:
                return 0
            if cache[i] != -1: # in backtracking, this gets computed many times
                return cache[i]
                # why am i seeing if we've visited this already?
            cache[i] = dfs(i + 1) + dfs(i + 2)
            return cache[i] # why am i returning cache[i]?   
        return dfs(0)
        
# n = 5
# 0, 1, 2, 3, 4, 5

#      5,  4,  3,  2,  1,  0
#. two one i