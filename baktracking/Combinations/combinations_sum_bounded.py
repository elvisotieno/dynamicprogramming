#Given a collection of candidte numbers(candidates) and a target
#Find all unique combinations that sum up to given target
# Each candidate may only be used once in the combinations
# NB The solution must not contain any duplicates
# Exaple: input = [10,1,2,7,6,1,5], target=8
# output = [[1,1,6],[1,7],[2,6],[1,2,5]]

#Solution Backtracking O(2^n)

def bounded_combinations_sum(candidates,target):
    #to avoid duplicates we sort our input array
    candidates.sort()
    result = []
    #curr_combinations will keep track of the current combinations
    # pos, keeps track of the index we are in our input array
    # curr_target keep track of the current target that we are summing up to because we keep subtracting...
    def backtrack(curr_combination,pos,curr_target):
        #1) base case we get a possible combination
        if curr_target==0:
            result.append(curr_combination.copy())
            return
        if curr_target<=0:
            return
        prev =-1
        for i in range(pos,len(candidates)):
            if candidates[i]==prev:
                continue
            # we decide to include it
            curr_combination.append(candidates[i])
            backtrack(curr_combination,i+1,curr_target-candidates[i])

            # we decide not to include it
            curr_combination.pop()
            prev = candidates[i]

    backtrack([],0,target)
    return result

print(bounded_combinations_sum([10,1,2,7,6,1,5],8))

