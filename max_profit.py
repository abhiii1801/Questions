class Solution:
    def maxProfit(self, p: List[int]) -> int:
        # max_profit = 0
        # for i in range(len(p)):
        #     for j in range(i+1, len(p)):
        #         max_profit = max(max_profit, p[j] - p[i])
        # return max_profit

        min_buy = float('inf')
        max_profit = 0

        for i, price in enumerate(p):
            min_buy = min(min_buy,price)
            max_profit = max(max_profit, price - min_buy)

        return max_profit



