from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)  # Adjacency list
        self.V = vertices              # Number of vertices
    
    def add_edge(self, u, v):
        self.graph[u].append(v)
    
    def topological_sort_dfs(self, v, visited, stack):
        visited[v] = True  # Mark the current node as visited
        
        # Recur for all vertices adjacent to this vertex
        for neighbor in self.graph[v]:
            if not visited[neighbor]:
                self.topological_sort_dfs(neighbor, visited, stack)
        
        stack.append(v)  # Push the current vertex to the stack
    
    def topological_sort(self):
        visited = [False] * self.V
        stack = []
        
        # Call the recursive helper function for all vertices
        for i in range(self.V):
            if not visited[i]:
                self.topological_sort_dfs(i, visited, stack)
        
        # Return the reversed stack as the topological order
        return stack[::-1]

# Example Usage:
g = Graph(6)
g.add_edge(5, 2)
g.add_edge(5, 0)
g.add_edge(4, 0)
g.add_edge(4, 1)
g.add_edge(2, 3)
g.add_edge(3, 1)

print("Topological Sort of the given graph:")
print(g.topological_sort())