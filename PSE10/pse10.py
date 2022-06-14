# You are given an integer array prices where prices[i] is the price of a given stock on the ith day.
# On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. 
# However, you can buy it then immediately sell it on the same day.
# Find and return the maximum profit you can achieve.


def max_profit(arr):
# initiate variable for profit between two days, set equal to 0
# initiate variable for totalProfit, set equal to 0
    totalProfit = 0
    profit = 0
    
    for i in range(len(arr)-1):
        if arr[i+1] > arr[i]:
            profit = arr[i+1] - arr[i]
            totalProfit += profit
    return totalProfit
            

# def alt_max_profit(arr):