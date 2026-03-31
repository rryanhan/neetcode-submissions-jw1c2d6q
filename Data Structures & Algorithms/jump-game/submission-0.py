class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False] * n
        dp[-1] = True

        for i in range(n-2, -1, -1):
            if nums[i] == 0:
                dp[i] = False
            for j in range(nums[i]+1):
                if dp[i + j]:
                    dp[i] = True
                    break
        return dp[0]
        