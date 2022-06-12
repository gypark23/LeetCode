class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        profit, maxprofit = 0, 0
        low = 0
        
        for high in range(len(prices)):
            profit = prices[high] - prices[low]
            maxprofit = max(maxprofit, profit)
            if(profit < 0):
                low = high
            
        return maxprofit
                