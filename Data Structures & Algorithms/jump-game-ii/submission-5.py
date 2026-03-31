class Solution:
    def jump(self, nums: List[int]) -> int:
        # dp represents min steps it takes to get to goal from i
        dp = [float("inf")] * len(nums)
        dp[-1] = 0
        for i in range(len(nums) - 2, -1, -1):
            for j in range(i + 1, i + 1 + nums[i]):
                if j < len(nums):
                    dp[i] = min(dp[i], 1 + dp[j])
        return dp[0]
        

# Bottom up solution         
#  2  1  3  2  1  0
#[ 2, 4, 1, 1, 1, 1]

# for loop, look for min dp[i + n] in the for loop