class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        #check the max of all possible states for prices [i]
        # if i sell -> i + 2
        # if i buy -> i + 1
        # dp[i][buying] for index and if i'm in buying/selling state

        # after buy/sell, increment i, flip the state
        # if im in cooldown, i + 1, dont flip the state

        #dp[i][buying]
        dp = [[0] * 2 for _ in range(len(prices) + 1)]

        for i in range(len(prices) - 1, -1, -1):
            for buying in [1, 0]:
                # we are buying
                if buying == 1:
                    buy = -prices[i] + dp[i + 1][0]
                    cooldown = dp[i + 1][1]
                    dp[i][1] = max(buy, cooldown)


                # we are selling
                if buying == 0:
                    # in range
                    if i + 2 < len(prices):
                        sell = prices[i] + dp[i + 2][1]
                    else:
                        sell = prices[i]
                    cooldown = dp[i + 1][0]
                    dp[i][0] = max(sell, cooldown)
        return dp[0][1]



        