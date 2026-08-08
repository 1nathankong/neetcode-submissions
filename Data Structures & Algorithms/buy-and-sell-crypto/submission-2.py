class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        min_profit=prices[0]
        for i in range(1,len(prices)):
            p=prices[i]
            if p>min_profit:
                profit = max(profit,-min_profit+p)
            else:
                min_profit=p
        return profit