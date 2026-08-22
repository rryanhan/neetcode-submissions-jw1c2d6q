class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[-1] = 1
        if len(dp) > 1:
            dp[-2] = 1 

        for i in range(n - 2, -1, -1):
            dp[i] = dp[i + 1] + dp[i + 2]
        return dp[0]
        
# n = 5
# 0, 1, 2, 3, 4, 5

#      5,  4,  3,  2,  1,  0
#. two one i

#dp[i] = number of distinct ways you can hit from dp[i + 1] + dp[i + 2]


# 0 1 2



# 0  1  2  3