# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        res = []
        def preOrder(node):
    
            if not node:
                return None
            res.append(node.val)
            preOrder(node.left)
            preOrder(node.right)

        preOrder(root)
        

        for i in range(1, len(res)):
            root.right = TreeNode(res[i])
            root.left = None
            root = root.right





        


        
        