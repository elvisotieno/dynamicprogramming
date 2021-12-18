#It is an important applications of graphs used to model many real-life problems
# where the beginning of a task is dependent on the completion of some other task.
#we may represent a number of jobs or tasks using nodes of a graph
#dependency is modeled through directed edges between nodes.
#If we want to perform a scheduling operation from such a set of tasks,
# we have to ensure that the dependency relation is not violated

import networkx as nx

dag = nx.digraph.DiGraph()

dag.add_nodes_from(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'])

dag.add_edges_from([('A', 'B'), ('A', 'E'), ('B', 'D'), ('E', 'C'),
                      ('D', 'G'),('C', 'G'),('C', 'I'), ('F', 'I')])

#We can now write a function to perform topological sorting using DFS
#We will begin at a node with no inward arrow, and keep exploring one of its branches until we hit a leaf node,
# and then we backtrack and explore other branches.
# Once we explore all the branches of a node, we will mark the node as ‘visited’ and push it to a stack.
# Once every node is visited, we can perform repeated pop operations on the stack to give us a topologically sorted ordering of the tasks.
def dfs(dag, start, visited, stack):
    if start in visited:
        # node and all its branches have been visited
        return stack, visited

    if dag.out_degree(start) == 0:
        # if leaf node, push and backtrack
        stack.append(start)

        visited.append(start)

        return stack, visited

    #traverse all the branches
    for node in dag.neighbors(start):
        if node in visited:
            continue

        stack, visited = dfs(dag, node, visited, stack)

    #now, push the node if not already visited
    if start not in visited:
        print("pushing %s"%start)
        stack.append(start)
        visited.append(start)
    return stack, visited


def topological_sort_using_dfs(dag):
    visited = []

    stack = []
    #first finds all nodes with no dependency
    start_nodes = [i for i in dag.nodes if dag.in_degree(i) == 0]

    #     print(start_nodes)

    # traverses each of them using the Depth First Search approach.
    for s in start_nodes:
        stack, visited = dfs(dag, s, visited, stack)

    print("Topological sorted:")

    #Finally, pop out values from the stack, which produces a topological sorting of the nodes.
    while (len(stack) != 0):
        print(stack.pop(), end=" ")


topological_sort_using_dfs(dag)
print("\nIf we look closely at the output order, we’ll find that whenever each of the jobs starts, "
      "it has all its dependencies completed before it.")

#compare this with the output of a topological sort method included in the ‘networkx’ module
# called ‘topological_sort()’.
topological_sorting = nx.topological_sort(dag)

for n in topological_sorting:

    print(n, end=' ')