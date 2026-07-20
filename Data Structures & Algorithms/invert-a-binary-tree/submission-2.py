# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        def dfs(node):
            if node.left and node.right:
                temp = node.right
                node.right = node.left
                node.left = temp
                return dfs(node.left) and dfs(node.right)
            elif node.left and not node.right:
                node.right = node.left
                node.left = None
                return dfs(node.right)
            elif node.right and not node.left:
                node.left = node.right
                node.right = None
                return dfs(node.left)
            else:
                return root
        
        return dfs(root)