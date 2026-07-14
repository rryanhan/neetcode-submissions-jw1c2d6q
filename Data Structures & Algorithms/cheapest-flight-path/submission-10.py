class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float("inf")] * n
        prices[src] = 0 # need to do this so first stop is 'reachable'

        for i in range(k + 1):
            tempPrices = prices.copy()

            for fromI, toI, priceI in flights:
                if prices[fromI] == float("inf"): # is the stop im at reachable from here?
                    continue
                tempPrices[toI] = min(priceI + prices[fromI], tempPrices[toI])
            
            prices = tempPrices
        
        return prices[dst] if prices[dst] != float("inf") else -1
                        