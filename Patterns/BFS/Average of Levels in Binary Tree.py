from collections import deque
class Solution:
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