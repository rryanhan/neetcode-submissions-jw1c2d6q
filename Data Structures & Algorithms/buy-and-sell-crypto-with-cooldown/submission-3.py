class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # State: buying or selling?
        # if buy -> i + 1
        # if sell -> i + 2

        # 1 for buy, 0 for sell
        dp = [[0] * 2 for _ in range(len(prices) + 1)] 

        for i in range(len(prices) - 1, -1, -1):
            for buying in [True, False]:
                # buying means i + 1
                if buying:
                    buy = dp[i + 1][0] - prices[i]
                    cooldown = dp[i + 1][1]
                    dp[i][1] = max(buy, cooldown)
                    

                # selling means cooldown, i + 2
                # if you sell, means you can buy right after
                else:
                    if i + 2 < len(prices):
                        sell = dp[i + 2][1] + prices[i]
                    else:
                        sell = prices[i]
                    # means you're selling, cant buy
                    cooldown = dp[i + 1][0]
                    dp[i][0] = max(sell, cooldown)
                
        
        return dp[0][1]

        