def knapSack(capacity, weight, val, n):
    dp = [[0 for x in range(capacity + 1)] for x in range(n + 1)]

    # Build table K[][] in bottom up manner
    for row in range(n + 1):
        for col in range(capacity + 1):
            if row == 0 or col == 0:
                dp[row][col] = 0
            elif weight[row - 1] <= col:
                dp[row][col] = max(val[row - 1]
                              + dp[row - 1][col - weight[row - 1]],
                              dp[row - 1][col])
            else:
                dp[row][col] = dp[row - 1][col]

    return dp


# Driver code
val = [1,4,5,7]
wt = [1,3,4,5]
W = 7
n = len(val)
print(knapSack(W, wt, val, n))

# This code is contributed by Bhavya Jain