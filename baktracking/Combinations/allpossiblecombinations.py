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