# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def getHeight(node):
            h = 0
            while node:
                h += 1
                node = node.left
            return h

        leftHeight = getHeight(root.left)
        rightHeight = getHeight(root.right)

        if leftHeight == rightHeight:
            return (1 << leftHeight) + self.countNodes(root.right)
        else:
            return (1 << rightHeight) + self.countNodes(root.left)
        