#1 Given two integers n and k, return all possible combinations of k numbers in the range(1,n)
# input: n=4, k=2, expected output=[(1,2),(1,3),(1,4),(2,3),(2,4),(3,4)]
class PossibleCombinations: #O(
    def combine(self, n,k):
        result=[]

        def backtracking(start,current_combination):
            #base case
            if len(current_combination) == k:
                result.append(current_combination.copy()) # we dont want to modify it after adding it to the result
                return
            # the decisions we need to make
            for i in range(start, n+1):
                current_combination.append(i)
                backtracking(i+1, current_combination)
                #doing clean up, we chose i, so we want to chose next element in our iteration
                current_combination.pop()

        backtracking(1,[])
        return result

first_combination=PossibleCombinations()
print(first_combination.combine(4,2))


# All possible arrangements satisfying a given condition
class ChaseGame:
    def n_queens(self,n):
        #all the information we need
        col =set()
        postive_diago=set()     #determined by (row+col)
        negative_diago=set()    #determined by (row-col)

        result=[]

        board = [["."]*n for row in range(n)]
        def backtracking(r):
            if r == n: #we were able to find valid n queents solution

                copy_board= ["".join(row) for row in board]
                result.append(copy_board)

                return
            #else we didn't reacg the base-case hence we need to continue
            #loop through the columns for the next row
            for c in range(n):
                if c in col or (r+c) in postive_diago or (r-c) in negative_diago:
                    continue
                col.add(c)
                postive_diago.add(r+c)
                negative_diago.add(r-c)
                board[r][c]= "Q"

                backtracking(r+1)

                col.remove(c)
                postive_diago.remove(r + c)
                negative_diago.remove(r - c)
                board[r][c] = "."

        backtracking(0)
        return result


queens=ChaseGame()
print(queens.n_queens(4))

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


