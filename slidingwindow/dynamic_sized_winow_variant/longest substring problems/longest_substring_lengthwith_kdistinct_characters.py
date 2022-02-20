# Given an array of characters, you are required to:
# find the length of the longest sub-string with k distinct characters

def longest_substring_length_k_distinnct_characters(arr: list, k: int) -> int:
    seen = {}
    start = 0
    longest_so_far = 0
    for end in range(len(arr)):
        seen[arr[end]] = seen.get(arr[end], 0) + 1
        if len(seen) <= k:
            current_length = len(arr[start:end+1])
            longest_so_far = max(longest_so_far, current_length)
        else:
            while len(seen) > k:
                left_char = arr[start]
                if seen[left_char] == 1:
                    seen.pop(left_char)
                else:
                    seen[left_char] -= 1
                start += 1

    return longest_so_far


arr = "BCAAAHHIBC"
k = 2
print(longest_substring_length_k_distinnct_characters(arr, k))
