#Given an array of distinct intergers candidates and a target interger target
# Return a list of all unique combination of candidates where the chosen numbers sum up to target.
#You may return combinations in any order
#Same number may be chosen unlimited number of times

#example: candiates =[2,3,6,7]
# Target = 7
#output =[2,2,3], [7]

# It is guaranteed that the number of unique combinations that sums up to given target is less than 150

def combination_sum(candidates,target):
    result = []

    # 1st pointer i, tells which of the candidates we're still allowed to choose
    # cur_combination current combinations that we've addeded so far
    # total keep track of the sum of our current combination, it indicates when we hit the target
    def dfs(i,cur_combinations,total):
        # 1st base cases: we found possible combinations
        if total == target:
            result.append(cur_combinations.copy()) # because we continously modify this variable
            return # so we dont continue beyond that tree

        #2nd base case: when we're unable to find possible combinations
        if i >= len(candidates) or total>target:
            return

        #Lets make a few decisions
        #1) we do include the candidate
        cur_combinations.append(candidates[i]) #update current combination
        dfs(i,cur_combinations, total+candidates[i])

        #2) we can't include any occurences of i
        cur_combinations.pop()
        dfs(i+1,cur_combinations, total)

    #now let's call our dfs

    dfs(0,[],0)
    return result

candiates = [2,3,6,7]
target = 7
print(combination_sum(candiates,target))




