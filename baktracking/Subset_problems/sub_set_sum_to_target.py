class SubsetProblems:
    def power_subset(self,nums):
        result = []

        current_subset=[]
        def backtrack(i):
            if i >= len(nums): # means we got a valid subset(base-case)
                result.append(current_subset.copy())
                return

            #decision to include nums[i]
            current_subset.append(nums[i])
            backtrack(i+1)

            #decision not to include nums[i]
            current_subset.pop()
            backtrack(i+1)

        backtrack(0)
        return result

    def subset_sum_to_target(self,arr,target):
        result = []


        def backtrack(weights):
            if sum(weights)==target: # we got a valid subset
                result.append(list(weights))
            other_weights = set(arr).difference(weights)
            #chosing weights in an increasing order to avoid duplication of results
            if len(weights)>0:
                other_weights = [W for W in other_weights if W > max(weights)]
            for weight in other_weights:
                # bounding function
                if sum(weights) + weight <= target:
                    #decision to include weight
                    weights.add(weight)
                    backtrack(weights)
                    #decision not to include weight
                    weights.remove(weight)


        backtrack(set())
        return result


all_possible_subsets = SubsetProblems()
nums = [1,2,3]
print(all_possible_subsets.power_subset(nums))
arr=[5,10,12,13,15,18]
target=30
print(all_possible_subsets.subset_sum_to_target(arr,target))