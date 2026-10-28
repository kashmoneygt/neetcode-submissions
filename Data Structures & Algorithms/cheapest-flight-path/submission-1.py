class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # cost to reach each airport
        prices = [float("inf")] * n
        prices[src] = 0

        for i in range(k + 1):
            updatedPrices = prices.copy()
            for s, d, p in flights:
                if prices[s] == float("inf"):
                    continue # can't reach this airport yet
                if prices[s] + p < updatedPrices[d]:
                    # found a cheaper way to reach d
                    updatedPrices[d] = prices[s] + p
            
            prices = updatedPrices

        return prices[dst] if prices[dst] != float("inf") else -1


