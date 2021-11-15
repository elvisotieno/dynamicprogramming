# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/



#Find Duplicates of array using bit array
# See GeeksforGeeks help at https://www.geeksforgeeks.org/find-duplicates-of-array-using-bit-array/
#You have an array of N numbers, where N is at most 32,000. The array may have duplicate entries and you do not know what N is. With only 4 Kilobytes of memory available, how would print all duplicate elements in the array ?.
# Examples:Input :
# arr[] = {1, 5, 1, 10, 12, 10}
# Output : 1 10
# 1 and 10 appear more than once in given
# array.
# Input : arr[] = {50, 40, 50}
# Output : 50
#solutions: There are two possible solutions
# one using hashtables and return elements whose value is >1
# Second using bit manipulation which is the most optimal solution considering the space constrain

# Python3 program to print all Duplicates in array

# A class to represent array of bits using
# array of integers
class BitArray:

    # Constructor
    def __init__(self, n):
        # Divide by 32. To store n bits, we need
        # n/32 + 1 integers (Assuming int is stored
        # using 32 bits)
        self.arr = [0] * ((n >> 5) + 1)

    # Get value of a bit at given position
    def get(self, pos):
        # Divide by 32 to find position of
        # integer.
        self.index = pos >> 5

        # Now find bit number in arr[index]
        self.bitNo = pos & 0x1F

        # Find value of given bit number in
        # arr[index]
        return (self.arr[self.index] &
                (1 << self.bitNo)) != 0

    # Sets a bit at given position
    def set(self, pos):
        # Find index of bit position
        self.index = pos >> 5

        # Set bit number in arr[index]
        self.bitNo = pos & 0x1F
        self.arr[self.index] |= (1 << self.bitNo)


# Main function to print all Duplicates
def checkDuplicates(arr):
    # create a bit with 32000 bits
    ba = BitArray(320000)

    # Traverse array elements
    for i in range(len(arr)):

        # Index in bit array
        num = arr[i]

        # If num is already present in bit array
        if ba.get(num):
            print(num, end=" ")

        # Else insert num
        else:
            ba.set(num)


# Driver Code
if __name__ == "__main__":
    arr = [1, 5, 1, 10, 12, 10]
    checkDuplicates(arr)
