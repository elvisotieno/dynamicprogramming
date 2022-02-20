# fixed-sized sliding window problem

def max_subarray_sum_size_k(arr:list,k:int)->int:
    max_so_far = 0
    start = 0
    end = k-1
    while end < len(arr):
        current_window = arr[start:end+1]
        current_window_sum= sum(current_window)
        max_so_far = max(current_window_sum,max_so_far)
        start += 1
        end += 1
    return max_so_far


arr = [4,2,1,7,8,1,2,8,1,0]
k=3
print(max_subarray_sum_size_k(arr,k))