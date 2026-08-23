class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [9999999] * (amount + 1)
        dp[0] = 0 # takes 0 coins to sum up to 0


        for i in range(amount + 1):
            for c in coins:
                # subtract amount - coins
                    # check if its > 0
                diff = i - c
                if diff >= 0:
                    dp[i] = min(dp[i], 1 + dp[diff]) # FIX
                # if we know how many coins it takes to hit diff, do dp[diff] + 1
        
        return dp[-1] if dp[-1] != 9999999 else -1

    



# dp[i] = the minimum number of coins needed to make amount i


#     12  11  10  9  8  7  6  5  4  3  2  1  0
#   1
#   5 
#  10
#
#