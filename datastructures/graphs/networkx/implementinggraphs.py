#https://likegeeks.com/depth-first-search-in-python/#Topological_sorting_using_Depth_First_Search
#Python offers a library to handle graphs called ‘networkx’.

#Constructing a graph in networkx
    #first create a graph object and then add all the nodes in the graph using the ‘add_node()’ method,
    # followed by defining all the edges between the nodes, using the ‘add_edge()’ method.
import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph() #create a graph
G.add_node(1) # add single node
G.add_node(2)
G.add_node(3)
G.add_node(4)
G.add_node(5)

G.add_nodes_from([6,7,8,9]) #add multiple nodes

#let’s define the edges between these nodes as shown in the figure.
# adding edges

G.add_edge(5,8)
G.add_edge(5,4)
G.add_edge(5,7)
G.add_edge(8,2)
G.add_edge(4,3)
G.add_edge(4,1)
G.add_edge(7,6)
G.add_edge(6,9)

#Graph traversal in networkx – DFS
dfs_output = list(nx.dfs_preorder_nodes(G, source=5))
print(dfs_output)
#Visualizing the graph in DFS using Matplotlib
nx.draw(G, with_labels=True, font_weight='bold')
plt.show()


