class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[-1] = nums[-1]

        for i in range(len(nums)-2, -1, -1):
            skip = dp[i + 1]
            if i + 2 < len(nums):
                take = nums[i] + dp[i + 2]
            else: 
                take = nums[i]
            dp[i] = max(skip, take)
        return dp[0]