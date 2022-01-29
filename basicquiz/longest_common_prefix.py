def longest_common_prefix(arr):
    result = ''
    smallest = min(arr,key=len)
    for char in smallest:
        for word in arr:
            running_prefix=result +char
            if running_prefix not in word:
                return result
        result+=char
    return result


arr=['dog','dogging','doggy']
print(longest_common_prefix(arr))