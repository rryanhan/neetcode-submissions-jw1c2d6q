class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0] * (len(text2)+1) for _ in range(len(text1)+1)]
        for i in range(len(text1) - 1, -1, -1):
            for r in range(len(text2) - 1, -1, -1):
                if text1[i] == text2[r]:
                    dp[i][r] = 1 + dp[i+1][r+1]
                else:
                    dp[i][r] = max(dp[i][r + 1], dp[i + 1][r])
        return dp[0][0]







# match -> dp[i][r] = 1 + dp[i+1][r+1]
# not match -> dp[i][r] max(dp[i][r + 1], dp[i + 1][r])
