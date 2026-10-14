class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price=prices[0]
        max_profit=0
        for val in prices[1:]:
            profit=val-min_price
            if val<min_price:
                min_price=val
            if profit>max_profit:
                max_profit=profit
        return max_profit
        