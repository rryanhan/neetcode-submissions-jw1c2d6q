class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # State: buying or selling?
        # if buy -> i + 1
        # if sell -> i + 2

        # 1 for buy, 0 for sell
        dp = [[-1] * 2 for _ in range(len(prices))] 

        def dfs(i, buying):
            if i >= len(prices):
                return 0
            if dp[i][buying] != -1 :
                return dp[i][buying]
            if buying == 1:
                buy = dfs(i + 1, not buying) - prices[i]
                cooldown = dfs(i + 1, buying)
                dp[i][buying] = max(buy, cooldown)
            else:
                sell = dfs(i + 2, not buying) + prices[i]
                cooldown = dfs(i + 1, buying)
                dp[i][buying] = max(sell, cooldown)
            return dp[i][buying]
        
        return dfs(0, 1)

        