class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m = 0
        for i in range(len(prices)-1):
            p = i + 1
            localMax = 0
            while p < len(prices):
                profit = prices[p] - prices[i]
                localMax = max(profit, localMax)
                p += 1
            m = max(localMax, m)
        return m
            


            

        