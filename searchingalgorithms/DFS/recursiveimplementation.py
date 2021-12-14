#Implementing Depth First Search a recursive approach
#We will define a base case inside our method, which is –
# If the leaf node has been visited, we need to backtrack.


def recursive_dfs(graph, source,path = []):
    if source not in path:
        path.append(source)

        if source not in graph:
            # leaf node, backtrack
            return path
        for neighbour in graph[source]:
            path = recursive_dfs(graph, neighbour, path)

    return path

graph = {"A":["B","C", "D"],
           "B":["E"],
           "C":["F","G"],
           "D":["H"],
           "E":["I"],
           "F":["J"]}
path = recursive_dfs(graph, "A")

print(" ".join(path))