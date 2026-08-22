class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        oneStep, twoStep = 0, 0

        for i in range(len(cost) - 1, -1, -1):
            temp = oneStep
            oneStep = cost[i] + min(oneStep, twoStep)
            twoStep = temp

        return min(oneStep, twoStep)


#  1  2  3

#  3  2  3 <- mincost