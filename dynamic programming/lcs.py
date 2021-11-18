#Longest Common Subsequence
# Longest sequence of string that have the longest fibonacci sequence
# First well define a function that returns a fibonacci sequence

# using dynamic programming
def fibonacci_dynamic(n):
    dp =[0 for x in range(n+1)]
    for i in range(n+1):
        if i==0:
            dp[i]=0
        elif i==1:
            dp[i]=1
        else:
            dp[i] =dp[i-1] + dp[i-2]
    return dp

fibonacci_dynamic(9)