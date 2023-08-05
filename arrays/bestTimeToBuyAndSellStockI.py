# approach is to sell the stock on the minimum price till ith date means take mini related to ith index and then take curr price
# compare if maxi is smaller than the nums[i] - mini price, means the profit is greater when we purchase on ith day and sell on mini day

def maxProfit(self, prices: List[int]) -> int:
    maxi = 0
    mini = prices[0]
    for price in prices:
        maxi = max(maxi, price - mini)
        mini = min(mini, price)
    return maxi
