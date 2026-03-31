class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        l, r = 0, 1

        while r < len(prices):
            if prices[r] > prices[l]:
                result = max(result, prices[r] - prices[l])
            else:
                l = r
            r +=1
        return result
            



# max
#
# 10   1   5   6   7   1
# l    r

# 10   1   5   6   7   1
#      l   r

# 10   1   5   6   7   1        5
#      l       r

# 10   1   5   6   7   1        6
#      l           r

# 10   1   5   6   7   1        6
#      l                  r
#
#
#
#
#
#
#
#
        