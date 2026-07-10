# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)

        toReturn = TreeNode(val)
        if val > root.val and not root.right:
            root.right = toReturn
            return root
        elif val < root.val and not root.left:
            root.left = toReturn
            return root
        else:
            if val > root.val:
                self.insertIntoBST(root.right, val)
            else:
                self.insertIntoBST(root.left, val)

        return root
