class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float("inf")] * (n + 1) # minimum # of squares it takes to reach x
        dp[0] = 0

        for target in range(1, n + 1):
            # need to subtract numbers from n until it hits zero

            # do we just go from n to 0 (use x), subtracting x^2 if its a sqrt
            for x in range(1, target + 1):
                square = x * x
                if square > target:
                    break # every value after won't work
                difference = target - square
                dp[target] = min(dp[target], 1 + dp[difference])
        
        return dp[n]

        # for up to n, how many numbers it takes to square to hit n
        # base case when n = 1, its one square
        

# 6 - 1 = 5

# 6 - 4 = 4


# 4
# 4 - 1
# 4 - 4 = 0