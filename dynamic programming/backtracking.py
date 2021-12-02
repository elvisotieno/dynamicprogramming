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


class ChaseGame:
    def n_queens(self,n):
        #all the information we need
        col =set()
        postive_diago=set()     #determined by (row+ol)
        negative_diago=set()    #determined by (row-col)

        result=[]

        board = [["."]*n for row in range(n)]
        def backtracking(r):
            if r == n: #we were able to find valid n queents solution

                copy_board= ["".join(row) for row in board]
                result.append(copy_board)

                return
            #else we didn't reacg the base-case hence we need to continue
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