#Implementing Depth First Search a non-recursive approach(iterative)
#https://likegeeks.com/depth-first-search-in-python/#Topological_sorting_using_Depth_First_Search
#We will use a stack and a list to keep track of the visited nodes.
#We’ll begin at the root node, append it to the path and mark it as visited.
#Then we will add all of its neighbors to the stack.
# At each step, we will pop out an element from the stack and check if it has been visited.
#If it has not been visited, we’ll add it to the path and add all of its neighbors to the stack.


def dfs_non_recursive(graph, source):
    if source is None or source not in graph:
        return "Invalid Input"
    path = []
    stack = [source]
    while (len(stack) != 0):
        s= stack.pop()
        if s not in path:
            path.append(s)

        if s not in graph:
            # leaf node
            continue
        for neighbor in graph[s]:
            stack.append(neighbor)

    return " ".join(path)

#Let’s define this graph as an adjacency list using the Python dictionary.

graph = {
    "A":["D","C","B"],
    "B":["E"],
    "C":["G","F"],
    "D":["H"],
    "E":["I"],
    "F":["J"]
}

DFS_path = dfs_non_recursive(graph, "A")
print(DFS_path)

