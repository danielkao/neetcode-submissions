# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        queue = deque()
        toReturn = []
        if root:
            queue.append(root)
        
        while len(queue) > 0:
            levelSize = len(queue)
            for i in range(levelSize):
                curr = queue.popleft()
                if i + 1 == levelSize:
                    toReturn.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
                
        return toReturn