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

print(fibonacci(100))

