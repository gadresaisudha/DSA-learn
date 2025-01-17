Graphs:
there are many types of graphs:
1. undirected grpahs:
This is where nodes can travle from both sides
2. directed graphs:
This is where you are allowed to go only in one direction provided by graph
3. Acyclic graph:
This does not have cycles cannot revisit the same node
4. directed Acyclic graph(DAG)
These are directed but are acyclic (no cycles)

In order for us to do a topological sort we need our graphs to be as directed acyclic graph.
Topology is like arrangement of nodes and connections
if we consider each node in DAG as task that needs to be completed but for this task to be completed it needs to complete all its dependencies
these dependencies are tasks to be completed before for completing the present node This is called indegree
no of connections coming to this node
and the dependencies that are going out of this node are outdegree
so now all topological sort is doing is convering all this graph form into linear arrangement where each task comes after its dependencies

Topological sort algorithm with DFS on DAG:
Approach with DFS
Using Depth First Search (DFS), the topological sort is achieved by leveraging the post-order traversal of the graph:

DFS Traversal: Start at an unvisited node, mark it as visited, and recursively visit all its adjacent unvisited nodes.
Push to Stack: After finishing the recursion for a node (i.e., when all its neighbors are visited), push it onto a stack.
Reverse Order: At the end, reverse the stack (or use it as is by popping elements in LIFO order) to get the topological order.
Algorithm
Here’s how it works step by step:

Initialize:
A boolean array visited to keep track of visited nodes.
A stack to store the nodes in topological order.
For each unvisited node in the graph, perform a DFS.
During the DFS, after visiting all neighbors of a node, push the node onto the stack.
At the end of the traversal, the stack contains the nodes in reverse topological order.

