#Longest Common Subsequence
# The task is to find the length of the longest Fibonacci-like subsequence of array
# If such subsequence does not exist, return 0
# First well define a function that returns a fibonacci sequence

# using dynamic programming

from functools import lru_cache
def fibonacci_sequence(n):
    dp =[0 for x in range(n+1)]
    for i in range(n+1):
        if i==0:
            dp[i]=0
        elif i==1:
            dp[i]=1
        else:
            dp[i] =dp[i-1] + dp[i-2]
    return dp

def longest_common_subsequence(s):
    columns = fibonacci_sequence(len(s))
    rows = list(s)
    dp_table= [[0 for x in range(len(columns))] for x in range(len(rows)+1)]

    columns.insert(0,0)
    rows.insert(0,0)

    for row in range(len(rows)):
        for col in range(len(columns)-1):
            if row ==0 or col ==0:
                dp_table[row][col]=0
            else:
                if int(rows[row]) == columns[col]:
                    dp_table[row][col] = 1 + dp_table[row-1][col-1]
                else:
                    dp_table[row][col]= max(dp_table[row-1][col], dp_table[row][col-1])
    return dp_table


def backtrack(table,col_total,row_total,X,Y):
    if row_total == 0 or col_total == 0:
        return set([""])
    elif X[row_total - 1] == Y[col_total - 1]:
        return set([Z + X[row_total - 1] for Z in backtrack(table, X, Y, row_total - 1, col_total - 1)])
    else:
        R = set()
        if table[row_total][col_total - 1] >= table[row_total - 1][col_total]:
            R.update(backtrack(table, X, Y, row_total, col_total - 1))
        if table[row_total - 1][col_total] >= table[row_total][col_total - 1]:
            R.update(backtrack(table, X, Y, row_total - 1, col_total))
        return R

s='1234577'
table= longest_common_subsequence(s)
Y= fibonacci_sequence(len(s))
X=list(s)
row_total= len(X)
col_total= len(Y)-1


#print(backtrack(table,X,Y,row_total,col_total))



