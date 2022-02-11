import heapq
from collections import Counter

def top_k_frequent_elements(nums: list, k:int) -> list:
    nums = [element *-1 for element in nums]
    hash = Counter(nums)
    # converting dictionary into list of tuples containing key_value pair
    # ensure you store them in(value,key) order since heapq use elements in first index
    given = [(value,key)for key, value in hash.items()]

    #Store the element-frequency pair in a Priority Queue
    heapq.heapify(given)
    largest=heapq.nlargest(k,given)
    output = [largest[i][1]*-1 for i in range(len(largest))]

    return output



nums=[1,1,3,2,2,3,4,3,4,4,4]
k=2
print(top_k_frequent_elements(nums,k))