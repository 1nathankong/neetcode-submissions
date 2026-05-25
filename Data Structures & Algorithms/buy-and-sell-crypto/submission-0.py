class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Example: 
        [10,1,5,6,7,1]

        first 2 pointer at idx 0 and 1: 1-9 = -8
        move second pointer, locations 0 and 2 5-10 = -5
        move second pointer, locations 9 and 3 6-10 ... all options all negative
        
        adjust all pointers and restart process: idx at 1 and 2: 5-1 = 4 profit!

        idx 1 and 3 6 - 1 profit!

        idx 1 and 4 7-1 profit

        repeat process until reach end

        """

        idx1 = 0
        idx2 = 1
        profit = 0
        while idx2 < len(prices):
            profit = max(profit, prices[idx2] - prices[idx1])
            idx2 += 1
            if idx2 == len(prices):
                idx1 += 1
                idx2 = idx1 + 1
        return profit
        