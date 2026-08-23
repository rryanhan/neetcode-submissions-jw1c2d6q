class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False] * n for _ in range(n)] # dp[left][right]
        res = 0

        for l in range(n - 1, -1, -1):
            for r in range(l, n):
                if l == r:
                    dp[l][r] = True
                elif r - l == 1:
                    dp[l][r] = s[l] == s[r]
                else:
                    dp[l][r] = dp[l + 1][r - 1] and s[l] == s[r]
                
                if dp[l][r]:
                    res += 1
        return res
        