#Given an array nums of distinct intergers, return all the possible permutations
#Generate a state-space tree
#Example: inpput = [1,2,3]
# Output: [1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]

def all_permutations(nums):
    result=[]

    #base case
    if len(nums)==1:
        return [nums[:]]
    for i in range(len(nums)):
        n = nums.pop(0)
        perms = all_permutations(nums)

        for perm in perms:
            perm.append(n)
        result.extend(perms)
        nums.append(n)
    return result

print(all_permutations([1,2,3]))