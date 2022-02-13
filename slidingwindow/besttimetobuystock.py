#You are given an array prices where prices[i] is the price of a given stock on the ith day.
#You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
#Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

def best_to_sell_buy_stock(A):
    n = len(A)
    L = 0
    R = 1
    max_profit = 0

    while R < n:
        if A[L] >  A[R]:
            L = R
            R +=1
        else:
            current_profit = A[R]-A[L]
            R +=1
            if current_profit > max_profit:
                max_profit = current_profit
    return max_profit

A=[7,6,4,3,1]
print(best_to_sell_buy_stock(A))