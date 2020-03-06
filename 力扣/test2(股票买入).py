class Solution:
    def maxProfit(self, prices):
        if len(prices)<=1:
            return 0
        sum = 0
        min_day = prices[0]
        for i in range(1, len(prices)):
            min_day = min(min_day, prices[i - 1])
            sum = max(prices[i] - min_day, sum)
        return sum


a = Solution()
print(a.maxProfit([]))
