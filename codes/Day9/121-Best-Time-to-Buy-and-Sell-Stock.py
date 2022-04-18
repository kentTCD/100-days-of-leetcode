class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1: return 0
        cur_mini = prices[0]
        cur_max = prices[1]
        cur_max_profit = cur_max - cur_mini
        
        for i in range(len(prices)-1):
            if prices[i] < cur_mini: cur_mini, cur_max = prices[i], prices[i+1]
            if prices[i+1] > cur_max: cur_max = prices[i+1]
            if cur_max - cur_mini > cur_max_profit: cur_max_profit = cur_max - cur_mini

        if cur_max_profit < 0: cur_max_profit = 0
        return cur_max_profit