class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maximum = 0
        l, r = 0, 0
        while r < len(prices):
            while r < len(prices) and prices[r] > prices[l]:
                price = prices[r] - prices[l]
                maximum = max(maximum, price) 
                r += 1 
            l = r
            r += 1
        return maximum


            
# 7 1 5 6 3 4
# 


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
        