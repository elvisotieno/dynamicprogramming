#Given an interger array nums and an interger K, return True if it is possible to divide this array into
# k non-empty subsets whose sums are equal
# Example input =[4,3,2,3,5,2,1] , K=4
# output= True
#Explanation: it's possible to divide it into 4 subsets (5),(1,4), (2,3),(2,3)
# First we compute the target value = sum(nums)/k


class Solution:
    def can_partition_to_k_subsets_of_equal_sum(self,nums,k):
        #let's improve on it
        if sum(nums) % k:
            return False
        nums.sort(reverse=True)
        target = sum(nums)/k
        already_used = [False]*len(nums)

        # we need to keep track of the index where we are(i)
        # k tracks how many partitions are left to build
        # curr_subset_sum tracks sum of our sub_sets so far
        def backtracking(i,k,curr_subset_sum):
            #1 base case
            if k==0:
                return True
            #2 base case
            if curr_subset_sum == 5:
                return backtracking(0,k-1,0)

            #implementing the main logic of our function
            for j in range(i,len(nums)):
                # skip that value if it's already been used or the resulting sum is bigger than our target
                if already_used[j] or curr_subset_sum + nums[j] > target:
                    continue

                already_used[j] = True
                if backtracking(j+1,k,curr_subset_sum+ nums[j]):
                    return True
                #do some clean-up
                already_used[j] = False
            return False
        return backtracking(0,k,0)

our_solution=Solution()
nums =[4,3,2,3,5,2,1]
k=4
print(our_solution.can_partition_to_k_subsets_of_equal_sum(nums,k))

