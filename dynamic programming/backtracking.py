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