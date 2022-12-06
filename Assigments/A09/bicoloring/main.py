### resources taken from geek for geeks 
### https://www.geeksforgeeks.org/bipartite-graph/?id=discuss

# Read the number of nodes
n = int(input())

# While the number of nodes is not 0
while n != 0:
    # Read the number of edges
    l = int(input())
    ##print(l)
    # Initialize a list of colors, where each element represents the color of the corresponding node
    colors = [-1] * n
    ##print(colors)
    # Iterate over the edges of the graph
    for i in range(l):
        # Read the two nodes of the edge
        u, v = map(int, input().split())
        ## print(u , v)
        # If the two nodes of the edge are uncolored, 
        # color the first one with the color 0 and the second one with the color 1
        if colors[u] == -1 and colors[v] == -1:
            colors[u] = 0
            colors[v] = 1
        # If the two nodes of the edge have the same color, it means the graph is not bicolorable
        elif colors[u] == colors[v]:
            print("NOT BICOLORABLE.")
            break
        # If the two nodes of the edge have different colors, simply continue to the next iteration

    # If all nodes are colored, it means the graph is bicolorable
    if all(colors):
        print("BICOLORABLE.")
    # Otherwise, it means there is at least one uncolored node, which means the graph is not bicolorable
    else:
        print("NOT BICOLORABLE.")

    # Read the next number of nodes
    n = int(input())