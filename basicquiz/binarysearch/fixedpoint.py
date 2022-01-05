#Given an array of n distinct integers sorted in ascending order,
# write a function that returns a Fixed Point in the array,
# if there is any Fixed Point present in array, else returns -1.
# Note that integers in array are unique and can be negative
#Python program to check fixed point
# in an array using binary search
def binarySearch(arr, low, high):
    if high >= low:

        mid = low + (high - low) // 2
        if mid == arr[mid]:
            return mid
        res = -1
        if mid + 1 <= arr[high]:
            res = binarySearch(arr, (mid + 1), high)
        if res != -1:
            return res
        if mid - 1 >= arr[low]:
            return binarySearch(arr, low, (mid - 1))

    # Return -1 if there is no Fixed Point
    return -1


# Driver program to check above functions */
arr = [-10, -1, 0, 3, 10, 11, 30, 50, 100]
n = len(arr)
print("Fixed Point is " + str(binarySearch(arr, 0, n - 1)))
