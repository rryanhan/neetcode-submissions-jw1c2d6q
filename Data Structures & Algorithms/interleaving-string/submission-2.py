class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        dp = [[False] * (len(s2) + 1) for _ in range(len(s1) + 1)]

        # dp[s1][s2]
        dp[len(s1)][len(s2)] = True

        for c1 in range(len(s1), -1, -1):
            for c2 in range(len(s2), -1, -1):
                if c1 == len(s1) and c2 == len(s2):
                    continue
                s3_index = c1 + c2
                #try taking from c1
                res1 = False
                if c1 < len(s1) and s3[s3_index] == s1[c1] and dp[c1 + 1][c2]:
                    res1 = True

                res2 = False
                # try taking from c2
                if c2 < len(s2) and s3[s3_index] == s2[c2] and dp[c1][c2 + 1]:
                    res2 = True
                dp[c1][c2] = res1 or res2
        return dp[0][0]

        



# at each position in s3, do we take from s1 or s2?

# dp[i][j] = 

# i represents the index we are at for s1
# j represents the index we are at for s2

# from these indices, can we continue to form s3?

# Can I match the next character using s1?
#                    OR
# Can I match the next character using s2?

# Starting at these two positions, can the remaining characters form the remainder of s3?

#    a   a   a   a
# b
# b
# b
# b
#
#
#
