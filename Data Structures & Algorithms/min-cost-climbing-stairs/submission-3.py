class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # top of the staircse is one beyond the last index
        oneStep, twoStep = cost[-2], cost[-1]


        for i in range(len(cost) - 3, -1, -1):
            minSteps = min(cost[i] + oneStep, cost[i] + twoStep)
            oneStep, twoStep = minSteps, oneStep
        return min(oneStep, twoStep)
# 2 options:
# 1 step or 2 step
# empty array is 0 step, so from there we do 1 step or 2 step to get into the problem
# keep track of dp[] of length(cost) + 1, dp[-1] is 0
# bottom up dp, updating with the min
# have edge cases to cover, making sure i + 1 and i + 2 are in bounds

# dp[i] = minimum cost to finish (reach the top) starting from stair
# dp[i] = min(cost[i] + dp[i + 1], cost[i] + dp[i + 2])

# [ 1, 2, 3 ] END