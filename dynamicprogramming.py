#So to summarize, any dp problem (once we figure out it is dp problem),
# the rows represent the elements and columns are the selection criteria (cumulative of elements) for the elements.
# And to figure out if it is dp problem:


# 1.(A) 0/1 Knapsack/backpack problem
# We know its a dynamic problem, because we are presented with elemenets to choose from,
# and we are expected to choose a subset that gives the maximum value without exceeding our capacity
# Use a 2D list to  construct our dp table:
# rows represent the elements(forms outer for loop)
# columns are the selection criteria (inner for loop) for the elements
# Once we populate our 2D list(matrix) we traceback and pick the elements that contribute to the maximum value

def elements_with_max_value(weight,value, capacity):
    N = len(weight)
    dp = [[0 for x in range(capacity + 1)] for x in range(N)]
    columns= capacity +1

    for row in range(N):
        given_weight=weight[row]

        for col in range(columns):
            total_weight= col

            if total_weight==0 or given_weight == 0:
                dp[row][col]=0

            elif row ==0 and total_weight >= given_weight:
                dp[row][col] = value[0]

            elif row > 0 and total_weight >= given_weight:
                dp[row][col] = max(value[row] + dp[row - 1][total_weight - given_weight], dp[row - 1][col])

            elif row>0 and total_weight < given_weight:
                dp[row][col] = dp[row - 1][col]

    max_value= dp[N-1][capacity]
    return max_value, dp
weight=[1,3,4,5]
value =[1,4,5,7]
capacity= 7
#print(elements_with_max_value(weight,value,capacity))


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