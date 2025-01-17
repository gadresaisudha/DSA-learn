"""
Graph theory :
Depth first search is the most fundamental search algorithm used to explore nodes(V) and edges(E) of the graph
Time Complexity - O(V+E)
Used to perform tasks such as count connected components, find bridges...

Basic DFS:
DFS plunges depth first into graph without regard for which edge it takes next until it cannot go any further 
at which point it backtracks and continues

"""

n = 8
Adajcency_list = { 1: [2, 3], 2: [1, 4, 5], 3: [1, 6], 4: [2], 5: [2, 7], 6: [3, 7], 7: [5, 6] }
#In above dict each key-value pair represent a node and its connecting nodes
visited = [False for i in range(n)]


def dfs(node):
    if visited[node]:
        return
    visited[node] = True

    neighbours = Adajcency_list[node]

    for next in neighbours:
        dfs(next)

    
dfs(1)

