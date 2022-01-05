#Given a collection of numbers, nums that might contain duplicates
# return all possible unique permutations that can be obtained,
# We need to transform our input array into a count hashmap

def permutations_duplicate_inputs(nums):
    result =[] #to store the result
    perm = [] #to store each permuatation
    count_hashmap = {n:0 for n in nums} #create hashmap with count initialized to 0
    #let's update our counts
    for n in nums:
        count_hashmap[n]+=1

    def dfs():
        #base case
        if len(perm)==len(nums):
            result.append(perm.copy())
            return
        for n in count_hashmap:
            #check if we have enough of it to choose from
            if count_hashmap[n] > 0:
                perm.append(n)
                count_hashmap[n] -= 1

                dfs()

                count_hashmap[n] += 1
                perm.pop()

    dfs()
    return result

print(permutations_duplicate_inputs([1,1,2]))
