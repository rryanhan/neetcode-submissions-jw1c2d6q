class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # cheapest cost for node i
        flighArray = [float("inf")] * n

        # costs 0 to start at starting flight
        flighArray[src] = 0


        for i in range(k + 1):
            tempFlights = flighArray.copy()
            for source, destination, cost in flights:
                # unreachable
                if tempFlights[source] == float("inf"):
                    continue
                tempFlights[destination] = min(tempFlights[destination], cost + tempFlights[source])
            flighArray = tempFlights
        
        return -1 if flighArray[dst] == float("inf") else flighArray[dst]
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # cheapest cost for node i
        prices = [float("inf")] * n

        # costs 0 to start at starting flight
        prices[src] = 0


        for i in range(k + 1):
            tempPrices = prices.copy()
            for source, destination, cost in flights:
                # unreachable
                if prices[source] == float("inf"):
                    continue
                tempPrices[destination] = min(tempPrices[destination], cost + prices[source])
            prices = tempPrices
        
        return -1 if prices[dst] == float("inf") else prices[dst]


        
    
# Bellman solution
# Each iteration i -> now allowing paths that use up to i flights
# - iteration 0 is using 0 edges, just src

# need an array -> prices = [infinity] * n
# array keeps track of for each node, the cheapest cost it takes to get there

# you can ONLY use edges whose starting node was reachable in previous node
# START prices[src] as 0
# iteration following will only be able to use flights that fly out of 0

        
    
# Bellman solution
# Each iteration i -> now allowing paths that use up to i flights
# - iteration 0 is using 0 edges, just src

# need an array -> prices = [infinity] * n
# array keeps track of for each node, the cheapest cost it takes to get there

# you can ONLY use edges whose starting node was reachable in previous node
# START prices[src] as 0
# iteration following will only be able to use flights that fly out of 0