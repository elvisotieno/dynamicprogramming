#So to summarize, any dp problem (once we figure out it is dp problem),
# the rows represent the elements and columns are the selection criteria (cumulative of elements) for the elements.
# And to figure out if it is dp problem:


# 1.(A) 0/1 Knapsack/backpack problem
# We know its a dynamic problem, because we are presented with elemenets to choose from,
# and we are expected to choose a subset that gives the maximum value without exceeding our capacity
# Use a 2D list to  construct our dp table:
# rows represent the elements(forms outer for loop)
# columns are the selection criteria (inner for loop) for the elements
# Once we populate our 2D list(matrix) we traceback and pick the elements that contribute to the maximum value

def elements_with_max_value(weight,value, capacity):
    N = len(weight)
    dp = [[0 for x in range(capacity + 1)] for x in range(N)]
    columns= capacity +1

    for row in range(N):
        given_weight=weight[row]

        for col in range(columns):
            total_weight= col

            if total_weight==0 or given_weight == 0:
                dp[row][col]=0

            elif row ==0 and total_weight >= given_weight:
                dp[row][col] = value[0]

            elif row > 0 and total_weight >= given_weight:
                dp[row][col] = max(value[row] + dp[row - 1][total_weight - given_weight], dp[row - 1][col])

            elif row>0 and total_weight < given_weight:
                dp[row][col] = dp[row - 1][col]

    max_value= dp[N-1][capacity]
    return dp
#weight=[1,3,4,5]
#value =[1,4,5,7]
#capacity= 7
#print(elements_with_max_value(weight,value,capacity))


def selected_elements(dp,profit):
    N =len(profit)
    output = [0 for x in range(N)]

    def recursion(max_so_far,current):
        if current == 0:
            return
        previous = current-1
        #Base case

        if max_so_far not in dp[previous]:
            output[current]= 1
            max_so_far = max_so_far - profit[current]
            current -=1
        else:
            current=previous

        recursion(max_so_far, current)

    recursion(dp[-1][-1],N-1)
    included_objects =[]
    for i in range(len(output)):
        if output[i]==1:
            included_objects.append(weight[i])
    return output,included_objects

weight=[1,3,4,5]
value =[1,4,5,7]
capacity= 8
dp = elements_with_max_value(weight,value,capacity)
print(selected_elements(dp,value))