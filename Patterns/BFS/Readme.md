Breath first search:
traverse the tree in level wise order
visit all nodes in each level

for this we are going to use the queue datastructure

when traversing through  the tree
visit all nodes in one level then by popping through each node add the child nodes to the queue
in this way you get to traverse through each level
Here in queue we are going to insert node
which has value and left and right pointers pointing to child

Binary Tree Level Order Traversal
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

Approach:
get queue DS from collections module
return null when root is empty
append root to the queue
now while queue is not empty
get the size of queue and
run another loop through this size and 
pop node append to the level_list and append its child nodes to the queue
finally after all values in queue are visited ie. appended to level_list then 
append this list to main res list

q = [3]
Iteration 1:
level_list = [3]
res = [[3]]
q = [9,20]

Iteration 2:
level_list = [9,20]
q = [15,7]
res = [3,[9,20]]...


solution:
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        q = deque()
        q.append(root)
        res = []
        while len(q):
            size = len(q)
            level_list = []
            for i in range(size):
                node = q.popleft()
                level_list.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                
            res.append(level_list)

        
        return res

Time Complexity: O(n)
Each node is being touch only once
Space Complexity:
O(n) -> worst case we might be holding n elements in the queue

Average of Levels in Binary Tree:
Given the root of a binary tree, return the average value of the nodes on each level in the form of an array. Answers within 10-5 of the actual answer will be accepted

Input: root = [3,9,20,null,null,15,7]
Output: [3.00000,14.50000,11.00000]
Explanation: The average value of nodes on level 0 is 3, on level 1 is 14.5, and on level 2 is 11.
Hence return [3, 14.5, 11].

Approach:
get queue DS from collections module
return null when root is empty
append root to the queue
now while queue is not empty
get the size of queue and
run another loop through this size and 
pop node append values to the sum_levellist and append its child nodes to the queue
Basically at one iteration time we will get all nodes that are at same level
finally after all values in queue are visited ie. appended to sum_levellist then calculate sum and append to the res

def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []
        
        q = deque()
        res = []
        q.append(root)

        while len(q):
            size = len(q)
            level_sum = 0
            for i in range(size):
                node = q.popleft()
                level_sum+=node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(level_sum/size)
        
        return res

Time Complexity: O(n)
Each node is being touch only once
Space Complexity:
O(n) -> worst case we might be holding n elements in the queue

3. Minimum depth of Binary tree:
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.
Input: root = [3,9,20,null,null,15,7]
Output: 2

Approach:
append root to the queue
level_height to keep track of height
while len(q) ->>
get the size of present q at that level
now loop on that level
pop elements
check if that particular element has left and right child nodes
if they are present add to the q
if both are not present return the level_height

def minDepth(self, root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    q = deque()
    level = 1
    q.append(root)
    while len(q):
        size = len(q)
        for i in range(size):
            node = q.popleft()
            if not node.left and not node.right:
                return level
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        level+=1

Time Complexity: O(n)
Each node is being touch only once
Space Complexity:
O(n) -> worst case we might be holding n elements in the queue