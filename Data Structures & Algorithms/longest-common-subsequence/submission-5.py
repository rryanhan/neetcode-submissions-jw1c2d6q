class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if not text1 or not text2:
            return 0
        
        dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]

        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
        return dp[0][0]




# base case
# empty strings have subset of 0

# 2 cases:
# (1) letters match
#    - add 1, see do i + 1 and j + 1
# (2) letters do not match
#    - 







# match -> dp[i][r] = 1 + dp[i+1][r+1]
# not match -> dp[i][r] max(dp[i][r + 1], dp[i + 1][r])
