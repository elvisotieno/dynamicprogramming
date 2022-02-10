import heapq

def kth_largest(nums,k):
    given = nums[:k]
    heapq.heapify(given)
    for i in range(k,len(nums)):
        node = heapq.heappop(given)
        largest = max(node,nums[i])
        heapq.heappush(given,largest)
    return heapq.heappop(given)

nums=[3,2,1,6,4,5]
k=2
print(kth_largest(nums,k))