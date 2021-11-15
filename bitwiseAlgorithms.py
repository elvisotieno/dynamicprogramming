import math

# using sqrt() method
def is_powof2(n):
    q= math.sqrt(n)
    if isinstance(q, int):
        return True
    if isinstance(q, float):
        return q.is_integer()
    return False

print(is_powof2(100))
# True

#using bit manipulation: we need to XOR it with a mask of 1 at the msb if the result is zero,
# then we conclude it is a pow of 2, else not power of  2

# from this I learn how to get the compliment of an interger
# by iterating over its binary representation and converting 0s to 1s and vise verser
def compliment_base_ten(N):
    answer= 0
    multiplier= 1 #takes care of which power of 2 we're at ie 2^0
    if N==0:
        return 1
    while N>0:
        # iterate the number accessing the current bit from lsb to msb
        current_bit= N&1
        # drop the bit at lsb by shifting to the right current_bit >>=1
        N >>= 1
        answer += multiplier * (1- current_bit)
        multiplier <<=1
    print(answer)

compliment_base_ten(9)


#Given an array of intergers where all the numbers appears twice except one
# How do we find that number:
# 1 Either by steping through the array and storing the prevous values in a has mapp Time and space coplexity O(n)
# 2 We can also use bit manipulation by just Xor everything

def lonely_interger(A):
    result=0
    for num in A:
        result ^=num

    print(result)

lonely_interger([9,1,2,3,4,2,3,4,9])