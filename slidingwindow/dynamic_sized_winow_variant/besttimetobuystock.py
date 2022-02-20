#You are given an array prices where prices[i] is the price of a given stock on the ith day.
#You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
#Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

def best_to_sell_buy_stock(A):
    n = len(A)
    start = 0
    max_profit = 0
    for end in range(1,n):
        current_profit = A[end]-A[start]
        if current_profit >=0:
            max_profit = max(current_profit,max_profit)
        else:
            while current_profit < 0:
                start += 1
                current_profit = A[end]-A[start]
    return max_profit


A=[7,1,4,6,3]
print(best_to_sell_buy_stock(A))