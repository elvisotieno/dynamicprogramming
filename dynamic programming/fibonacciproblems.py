#509. Fibonacci Number
#The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence,
# such that each number is the sum of the two preceding ones, starting from 0 and 1.
# The question is: Given n, calculate F(n)

#Bottom down approach(using explicit memoization)

fib_cache ={}
def fib(n):
    #if we've catched the value then return it
    if n in fib_cache:
        return fib_cache[n]
    #compute the nth term
    #define our base case
    if n <= 0:
        value= 0
    elif n == 1:
        value= 1

    else:
        value = fib(n-1) + fib(n-2)

    #catch and return its value
    fib_cache[n]=value
    return value

#print(fib(10))

#Using @lru catch library from python functool
from functools import lru_cache

@lru_cache(maxsize=1000)
def fibonacci(n):
    if n==1:
        return 1
    elif n<=0:
        return 0
    else:
        return fibonacci(n-1) + fibonacci(n-2)
n=4
print(f'fib of {n} is {fibonacci(4)}')


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
    print(dp)
    print(f'fibonacci of {n} is: {dp[-1]}')


fibonacci_dynamic(100)

# Longest sub_array that have fibonacci sequence, if no fibonacci sequence  in the array return false
# The idea is to write a program that returns all the fibonacci sequence upto  the largest element in the array
# then write a program that returns all the substrings from the given array
#finally we iterate through the substrings and check if its in the sequence and keep track of the global max

class LongestFibonacciSequence:
    #def __init__(self,arr):
        #arr = self.arr

    def fibonacci_sequence(self, arr):
        n = arr[-1]
        sequence = [0 for x in range(n + 1)]
        for i in range(n + 1):
            if i == 0:
                sequence[i] = 0
            elif i == 1:
                sequence[i] = 1
            else:
                sequence[i] = sequence[i - 1] + sequence[i - 2]
        return (sequence)


    def all_subarrays(self,arr):
        return [[arr[col:col + row] for col in range(len(arr) - row + 1)] for row in range(1, len(arr))]



    def check_longest_substring_fibsequence(self, arr):
        allsubarrays= self.all_subarrays(arr)
        sequence  = self.fibonacci_sequence(arr)
        global_max=0

        for subarrays in allsubarrays:
            for subarray in subarrays:
                if set(subarray).issubset(set(sequence)):
                    current= len(subarray)
                    if current> global_max:
                        global_max=current
        return global_max


longest = LongestFibonacciSequence()
arr= [1,2,3,4,5,6,7,8]
print(longest.check_longest_substring_fibsequence(arr))

#3 Count all possible paths from top left to bottom right of a mXn matrix
#The question is how many paths are there from the top left to the bottom right

#SolutionA(using dynamic programming)
def matrix(m,n):
    dp=[[0 for col in range(m + 1)] for row in range(n+1)]
    dp[1][2]=1
    dp[2][2]=1
    dp[2][4]=1
    dp[3][0]=1
    dp[4][3]=1
    dp[4][4]=1
    dp[5][4]=1
    return dp

def all_pathsfrom_left_topto_bottom_left(m,n):
    grid = matrix(m,n)
    result_grid=[[0 for col in range(m + 1)] for row in range(n+1)]
    for row in range(m,-1,-1):
        for col in range(n,-1,-1):
            if row==m and col==n:
                result_grid[row][col]=1
            elif row ==m:
                result_grid[row][col]=1
            elif col ==n:
                result_grid[row][col]=1
            elif grid[row][col]==1:
                result_grid[row][col]=0
            else:
                result_grid[row][col]= result_grid[row][col+1] + result_grid[row+1][col]
    return result_grid[0][0]



print(all_pathsfrom_left_topto_bottom_left(10,10))