Trees are just type of graph:

Two types of graphs we deal with generally:
1. graphs that are trees:
Basically they are acyclic and connected
that means nodes are connected but do not have cycle
that means every node in graph can reach the other node

2. graphs that aren't trees
nodes are connected and also have cycles


Traversals for trees:(graphs that are acyclic connected)
1. Inorder(left,root,right)
2. preorder(root,left,right)
3. postorder(left,right,root)

In trees there is no possibility of visiting  a node twice. as there is no cycle

mostly we do a inorder traversal
so visit complete left, then the root then the right


now coming to graphs that has cycles:
there is posibility of visiting node twice in graph
we need to keep track of visited node 
so when we need to go from one node to another we check if it is visited or not and go to unvisited node

if there is no way to go from that node as they have already been visited and you have some unvisited nodes backtrack to the nodes that hasnt been visited yet
once you have visited all backtrack to the start node


Number of Islands:
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Here you can use DFS
like pick one node and visit all adjacent nodes 
count this whole as one island
continue this process



class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, columns = len(grid),len(grid[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        res = 0
        def dfs(r,c):
            
            if r<0 or c<0 or r>=rows or c>=columns or grid[r][c]=="0":
                return
            
            grid[r][c] = "0"
            for dr,dc in directions:
                dfs(r+dr,c+dc)
        


        for i in range(rows):
            for j in range(columns):
                if grid[i][j]== "1":
                    dfs(i,j)
                    res+=1

        
        return res