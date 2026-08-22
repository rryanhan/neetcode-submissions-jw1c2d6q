class Solution:
    def climbStairs(self, n: int) -> int:
        oneStep = 1
        twoStep = 1

        for _ in range(n - 1):
            temp = oneStep
            oneStep = temp + twoStep
            twoStep = temp
        return oneStep
        


# ?  ?  ?  1  1
# 0  1  2  3  4