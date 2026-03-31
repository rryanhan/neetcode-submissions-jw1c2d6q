class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n+1)
        dp[-1] = 1

        for i in range(n-1, -1, -1):
            if i + 2 > n:
                dp[i] = dp[i + 1]
            else:
                dp[i] = dp[i + 1] + dp[i + 2]
        return dp[0]
        
# n = 5
# 0, 1, 2, 3, 4, 5