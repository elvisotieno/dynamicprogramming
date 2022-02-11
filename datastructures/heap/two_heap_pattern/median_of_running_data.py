import heapq


class FindMedian:
    def __init__(self):
        #initializing the two heaps
        self.small, self.large = [],[]

    def add_to_heaps(self,num:int)->None:
        heapq.heappush(self.small,num)

        #Let's make a few decisions
        #1)make sure that every num in small is less than nums in large
        if self.small and self.large and (-1*self.small[0])>self.large[0]:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large,val)

        #2) make sure sizes are within acceptable limits
        if len(self.small)> len(self.large)+1:
            val = -1*heapq.heappop(self.small)
            heapq.heappush(self.large,val)

        if len(self.large)> len(self.small)+1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small,val*-1)

    def get_median(self)->float:
        #2 base case the length of numbers are even or odd
        #a) check for odd
        if len(self.small)>len(self.large):
            return self.small[0]
        if len(self.large)>len(self.small):
            return self.large[0]
        return -1*(-1*self.small[0]+self.large[0])/2


    def median_running_data(self,nums:list)->float:
        for num in nums:
            self.add_to_heaps(num)
        median = self.get_median()
        return median

nums=[2,3,4,7,9]
test = FindMedian()
print(test.median_running_data(nums))