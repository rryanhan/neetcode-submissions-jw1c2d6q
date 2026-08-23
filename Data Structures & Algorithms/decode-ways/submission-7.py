class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0] * (len(s) + 1)
        dp[-1] = 1

        for i in range(len(s) -1, -1, -1):
            if s[i] == "0":
                dp[i] = 0
            # can it be decoded as a single digit?
            else:
                dp[i] += dp[i + 1]

            # can it be decoded as a double digit?
                # check if it is in range
            if i + 1 < len(s) and 10 <= int(s[i : i + 2]) <=26:
                dp[i] += dp[i + 2] 

        return dp[0]
    


# s =  1  0  1  2  NOTHING
# dp =[0, 0, 0, 0, 1]


# rules:
    # if the s starts with a 0, zero ways to decode from here

    # if s starts with a 1 or 2, that's +1 ways to decode on top of what 
    # we already have

    # question to ask:
        # with the given s, can we build with one character, and two 
        # character?

#   1   0   1   2
#  ..?   0   2   1
#   ^ <- what happens here? i + 1 is 0