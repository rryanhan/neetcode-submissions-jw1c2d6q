class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # top of the staircse is one beyond the last index
        dp = [0] * (len(cost)+1)
        dp[-1] = 0

        for i in range(len(cost) - 1, -1, -1):
            curCost = cost[i]
            if i + 2 > len(cost):
                dp[i] = cost[i] + dp[i + 1]
            else: 
                dp[i] = min((cost[i] + dp[i + 1]), (cost[i] + dp[i + 2]))
        return min(dp[0], dp[1])
        
# 2 options:
# 1 step or 2 step
# empty array is 0 step, so from there we do 1 step or 2 step to get into the problem
# keep track of dp[] of length(cost) + 1, dp[-1] is 0
# bottom up dp, updating with the min
# have edge cases to cover, making sure i + 1 and i + 2 are in bounds

# dp[i] = minimum cost to finish (reach the top) starting from stair
# dp[i] = min(cost[i] + dp[i + 1], cost[i] + dp[i + 2])