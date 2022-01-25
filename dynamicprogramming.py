







#Extended Knapsack Problem
#Given N items, each item having a given weight Ci and a profit value Pi,
# the task is to maximize the profit by selecting a maximum of K items adding up to a maximum weight W
# consider a 3-dimensional table dp[N][W][K], where N is the number of elements,
# W is the maximum weight capacity and K is the maximum number of items allowed in the knapsack.

#Kadanes Algorithm
def max_subarray_sum(A):
    n = len(A)
    dp =[[0 for x in range(n)] for x in range(2)]

    #base case
    current_sum = A[0]
    global_sum = A[0]
    dp[0][0]=current_sum
    dp[1][0]= global_sum

    for i in range(1,n):
        current_sum = max(A[i], current_sum+A[i])
        dp[0][i]=current_sum

        if current_sum > global_sum:
            global_sum = current_sum

        dp[1][i] = global_sum

    return global_sum, dp
Array=[-2,1,-3,4,-1,2,1,-5,4]
#print(max_subarray_sum(Array))


def coin_change(arr,change):
    n = len(arr)
    dp = [[0 for x in range(change + 1)] for x in range(n)]
    # iterate and fill our dp with all posible donominations
    for row in range(n):
        given_coin = arr[row]
        for col in range(change+1):
            total_change = col
            if row == 0:
                dp[row][col] = total_change//arr[row]
            elif row > 0 and given_coin > total_change:
                dp[row][col] = dp[row-1][col]
            elif row > 0 and given_coin <= total_change:
                dp[row][col] = min(total_change//given_coin + dp[row-1][total_change % given_coin],
                                   dp[row-1][col])


    return dp



def get_change_denomination(arr,change):
    if change < 1:
        return 0
    dp = coin_change(arr,change)
    required_denominations = {}
    min_coins = dp[len(arr)-1][change]
    if min_coins == dp[len(arr)-2][change]:
        res_dominions = arr[0:len(arr)-1]
    else:
        res_dominions = arr[0: len(arr)]

    while min_coins > 0:
        current = res_dominions.pop()
        if change//current >0:
            required_denominations[current] = change//current
            min_coins = min_coins - change//current
            change = change% current

    return dp[len(arr)-1][capacity], required_denominations
arr =[1,3,4]
change =7

print(get_change_denomination(arr,change))