# Source: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

# Problem: "Best Time to Buy and Sell Stock"

# Example: Say you have an array for which the ith element is the price of a given stock on day i.
#   Design an algorithm to find the maximum profit by buying and selling stocks

# Approach 1: If I could buy and sell only once

# Approach 2: If I could buy and sell as much as I wanted

def bestTimeBuySellStockSol1(prices):
	if not prices:
		return None

	minValue = sys.maxsize
	maxProfit = 0

	for stock in prices:
		if stock < minValue:
			minValue = stock
		maxProfit = max(maxProfit, stock - minValue)

	return maxProfit

def bestTimeBuySellStockSol2(prices):
    if not prices or len(prices) < 2:
        return 0
    maxProfit = 0
    prev = 0
    while prev+1 < len(prices) and prices[prev] > prices[prev+1]:
        prev += 1
    for i in range(prev,len(prices)-1):
        if prices[i+1] > prices[i]:
            maxProfit += prices[i+1]-prices[i]
    return maxProfit