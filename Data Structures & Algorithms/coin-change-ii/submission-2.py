class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # col of length amount + 1 to account for base case
        # row of lengh coins + 1, in the case we have 0 coins
        dp = [[0] * (amount + 1) for _ in range(len(coins) + 1)]

        for i in range(len(coins) + 1):
            # [row i] [col 0] = 1
            dp[i][0] = 1
        
        # don't need to cover i = len(coins) because base case is already done
        for i in range(len(coins) - 1, -1, -1):
            for a in range(amount + 1):
                # skip the coin
                # DONT DO += AS THERE MAY BE NONZEROES
                dp[i][a] = dp[i + 1][a]

                # take the coin, a has to be >= coins[i]
                if a >= coins[i]:
                    dp[i][a] += dp[i][a - coins[i]]
        return dp[0][amount]


