class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # an array of dictionaries
        # dictionary has:
           # index -> {sum : how many ways we can reach it}
        # more than one dictionary per index
        # [
        #   {} , i = 0
        #   {} , i = 1
        #   {}   i = 2 ... etc
        # ]
        dp = [defaultdict(int) for _ in range(len(nums) + 1)]
        # dp[index][sum] = total
        dp[0][0] = 1

        # i is the number i am at
        for i in range(len(nums)):
            # we get all possible sums at current i
            for total, ways in dp[i].items():
                dp[i + 1][total + nums[i]] += ways
                dp[i + 1][total - nums[i]] += ways
        return dp[len(nums)][target]

        