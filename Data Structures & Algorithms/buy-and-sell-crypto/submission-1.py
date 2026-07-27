class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        temp = 0
        for i in range(len(prices)-1):
            m = max(prices[i+1:])
            if m > prices[i]:
                profit = m - prices[i] if m - prices[i] > profit else profit
        return profit

        