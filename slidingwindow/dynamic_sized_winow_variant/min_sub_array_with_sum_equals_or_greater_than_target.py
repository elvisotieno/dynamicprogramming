# minimum sub_array with sum greater or equal to a given target

def min_sub_array(arr:list,target:int)->int:
    min_size=len(arr)
    global_window_sum = 0
    start = 0
    for end in range(len(arr)):
        global_window_sum += arr[end]
        while global_window_sum >= target:
            min_size = min(len(arr[start:end+1]), min_size)
            global_window_sum -= arr[start]
            start +=1
    if min_size ==len(arr):
        return None
    return min_size

arr =[4,2,2,7,8,1,2,8,1,0]
target=30
print(min_sub_array(arr,target))
